
import numpy as np
import cv2

import os
from multiprocessing import Process

url = "rtsp://user:password@ip:port/stream"
def run():
    capture = cv2.VideoCapture(cv2.CAP_FFMPEG)
    capture.open(url)
    while True:
        result, frame = capture.read()
        if result == False:
        	print('get frame fail')
        	break
        cv2.imshow('video', frame)
        if cv2.waitKey(1) == ord("q"):
            break
         
if __name__ == '__main__':
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
    p = Process(target=run)
    p.start()
    p.join()
