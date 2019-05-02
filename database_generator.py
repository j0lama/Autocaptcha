import cv2
import numpy as np
import requests
import matplotlib.pyplot as plt

url = 'https://www.megadede.com/captcha/flat'


for i in range(100):
	img_data = requests.get(url).content
	with open('flat.png', 'wb') as handler:
	    handler.write(img_data)

	img = cv2.imread('flat.png')
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, umbralizacion = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	kernel = np.ones((3, 3), np.uint8)
	cierre = cv2.morphologyEx(umbralizacion, cv2.MORPH_CLOSE, kernel)

	print(cierre.shape)

	for j in range(5):
		plt.ion()
		plt.imshow(cierre[:,60*j:60*(j+1)])
		#cv2.imshow('image',cierre[:,60*j:60*(j+1)])
		#cv2.waitKey(1)
		num = input('Introduce el numero de la imagen: ')
		resize = cv2.resize(cierre[:,60*j:60*(j+1)], (40, 30))
		img_name = 'database/' + str(i) + '_' + str(j) + '_' + num + '.png'
		cv2.imwrite(img_name, resize)
