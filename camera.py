from picamzero import Camera
from pyzbar import pyzbar
import cv2
import pygame

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame)
    ret = []
    for qrcode in qrcodes:
        x, y, w, h = qrcode.rect
        qrcode_text = qrcode.data
        ret.append((qrcode_text, x, y, w, h))
    return ret

images = []
for i in range(4):
    for j in range(8):
        images.append(pygame.image.load(f"karte/{i}-{j}.webp"))

camera = Camera()
camera.still_size = (800, 600)

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    numpy_img = camera.capture_array()
    scale = 1
    w, h = int(numpy_img.shape[1]*scale), int(numpy_img.shape[0]*scale)
    codes = read_qrcodes(cv2.resize(numpy_img, (w, h), interpolation=cv2.INTER_LINEAR))

    screen.fill("white")
    screen.blit(pygame.transform.rotate(pygame.surfarray.make_surface(numpy_img), 90), (0, 0))
    for code in codes:
        text, x, y, w, h = code
        screen.blit(pygame.transform.scale(images[int(text)], (w, h)), (x, 600-y-h))
    pygame.display.flip()

    print("test")
pygame.quit()

