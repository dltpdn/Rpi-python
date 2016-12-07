import cv2
import base64

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
r, data = cam.read()
#print r, data
if r:
    cv2.imshow('img',data)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    
    r, enc = cv2.imencode('.png', data)
    b64 = base64.encodestring(enc)
    print b64
#frame = cam.read()[1]
#cnt = cv2.imencode('.png',frame)[1]
#b64 = base64.encodestring(cnt)
#print b64

