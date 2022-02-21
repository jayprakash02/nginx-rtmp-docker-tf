import cv2

rtmp_server='rtmp://127.0.0.1:1935/live/test'
cap = cv2.VideoCapture(rtmp_server)

if not (cap.isOpened()):
    print ('Could not open video device')
else:
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    while(True):
        ret, frame = cap.read()
        cv2.imshow('preview',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()