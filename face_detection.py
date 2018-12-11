'''
face_detection_image.py
Este archivo contiene el metodo detect el cuale permiten reconocer e nameentificar
un rostro en una imagen
'''
import numpy as np
import cv2 as cv
import face_recognition
import pickle

#Imagenes representadas en caracteristicas
#data = pickle.loads(open(args["encodings"], "rb").read())
#Variable que refiere al clasificador haarcascade de rostros frontales
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# carga el archivo de caracteristicas de la db
data= pickle.loads(open("encodings.pickle", "rb").read())
    
'''
detetct
@Input: imagen en formato numpy array
Metodo que recibe una imagen y detecta quien es la persona en la imagen
@return: nombre de la persona en la foto
'''
def detect(img): 
	type(data)
	#Obtiene los componentes a color y gris de la imagen
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

	# detecta caras en escala de grises
	rects = face_cascade.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30),
		flags=cv.CASCADE_SCALE_IMAGE)

	# Recorta las caras
	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

	# Utiliza el modulo de face recognition con las caras recortadas
	foundEncodings = face_recognition.face_encodings(rgb, boxes)
	names = []

	# Itera en las caracteristicas encontradas
	for encoding in foundEncodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		# Verifica si encuentra coincidencias
		if True in matches:
			
			# Encuentra los indices de todas las coincidencias para contar el total de
			# veces que cada cara fue encontrada
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# Itera en las coincidencias y adiciona un contador para cada cara reconocida
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# Determina la cara recconocida (nombre) evaluando el mayor numero de conteos
			name = max(counts, key=counts.get)
		
		# Adiciona los nombres encontrados a la lista
		names.append(name)
		return(names[0])



