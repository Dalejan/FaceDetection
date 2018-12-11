# ##Conversion de archivos binarios a imagenes
import re
import base64
from PIL import Image
import io
import cv2 as cv
import numpy as np

# Face detection
from face_detection import detect 

#Convierte imagen en formato base64 a np array
def b64ToImg(base64_string): 
    imgstr = re.search(r'base64,(.*)', base64_string).group(1)
    image_bytes = io.BytesIO(base64.b64decode(imgstr))
    im = Image.open(image_bytes)

    return cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)

#Toma foto y detecta la cara
def onPhoto():
    #test1 = imagen en formato base64 de alejandro
    #test2 = imagen en formateo base54 de obama
    img = b64ToImg(open("test_2", "rb").read())
    id = detect(img)
    if id is None:
        print "Nada"
    else:
        print id

onPhoto()