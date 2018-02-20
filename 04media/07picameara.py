import time
import picamera

with picamera.PiCamera() as camera:
    try:
        camera.start_preview()
        while True:
            shutter = eval(input('insert key when you are ready to take photo. [photo:1, video:2] '))
            now_str = time.strftime("%Y%m%d-%H%M%S")
            if shutter == 1:
                camera.capture('/home/pi/demo/camera/photo%s.gif' %now_str)
            elif shutter == 2:
                camera.start_recording('/home/pi/demo/camera/video%s.h264' %now_str)
                input('insert key when you want to stop recoding.')
                camera.stop_recording()
    finally:
        camera.stop_preview()
    