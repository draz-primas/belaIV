from picamzero import Camera
from pyzbar import pyzbar
import cv2

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.QRCODE])
    return qrcodes

def start():
    camera = Camera()
    camera.still_size = (800, 600)

def get_codes(scale):
    numpy_img = camera.capture_array()
    w, h = int(numpy_img.shape[1]*scale), int(numpy_img.shape[0]*scale)
    codes = read_qrcodes(cv2.resize(numpy_img, (w, h), interpolation=cv2.INTER_LINEAR))
    return codes
