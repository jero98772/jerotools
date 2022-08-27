import cv2
import matplotlib.image as mpi
import matplotlib.pyplot as plt
import numpy as np

def img(file):
    datos = mpi.imread(file)
    return datos
def lessBrightness(imagen,factor):
	height = imagen.shape[0]
	width = imagen.shape[1]
	img = np.zeros((alto,ancho,3),dtype=int)
	for i in range(height):
		for j in range(width):
			for k in range(3):
				img[i][j][k] =imagen[i][j][k]//factor 
	return img
def show(datos):
    f = plt.figure()
    f.add_subplot(1,2,1)
    plt.imshow(datos)
    plt.show()
def negative(imagen):
	height = imagen.shape[0]
	width = imagen.shape[1]
	img = np.zeros((height,width,3),dtype=int)
	for i in range(height):
		for j in range(width):
			img[i][j][0] = abs(imagen[i][j][0]-255)
			img[i][j][1] = abs(imagen[i][j][1]-255)
			img[i][j][2] = abs(imagen[i][j][2]-255)
	return img
def mirror(imagen):
	height = imagen.shape[0]
	width = imagen.shape[1]
	img = np.zeros((height,width,3),dtype=int)
	for i in range(width):
		for j in range(height):

			img[j][width-i-1] = imagen[j][i]
	return img
def rotate90(imagen):
	height = imagen.shape[0]
	width = imagen.shape[1]
	img = np.zeros((alto,width,3),dtype=int)
	for i in range(height):
		for j in range(ancho):
			img[j][i][0] = imagen[i][j][0]
			img[j][i][1] = imagen[i][j][1]
			img[j][i][2] = imagen[i][j][2]
	return img
def grayScale(imagen):
	height = imagen.shape[0]
	width = imagen.shape[1]
	img = np.zeros((height,width,3),dtype=int)
	for i in range(height):
		for j in range(width):
			elemento1 = imagen[i][j][0]
			elemento2 = imagen[i][j][1]
			elemento3 = imagen[i][j][2]
			prom = elemento1+elemento2+elemento3/imagen.shape[2]
			for k in range(3):
				img[i][j][k] = prom
	return img

def minimo_divisor_mayor_a_uno(num):
	if num % 2 == 0:
		return 2
	else:
		div= 3
		for i in range(3,num,2):
			if num % i == 0:
				div = i
				break
	return div 
def meanImage(col_incio,fil_incio,col_final,fil_fin,imagen):
	rprom = 0
	gprom = 0
	bprom = 0	
	total_pixeles = (col_final-col_incio)*(fil_fin-fil_incio)	
	for i in range(fil_incio,fil_fin+1):
		for j in range(col_incio,col_final+1):
			#color = promedio_para_img(i,j,i+alto,j+ancho,img)
			rprom += imagen[i][j][0]
			gprom += imagen[i][j][1]
			bprom += imagen[i][j][2]	
	rprom /= total_pixeles
	gprom /= total_pixeles
	bprom /= total_pixeles
	return [rprom,gprom,bprom ]
def pixelar(imagen):
	height = imagen.shape[0]
	width = imagen.shape[1]
	altojump = minimo_divisor_mayor_a_uno(imagen.shape[0])
	anchojump = minimo_divisor_mayor_a_uno(imagen.shape[1])

	img = np.zeros((height,width,3),dtype=int)
	for i in range(altojump,height):
		for j in range(anchojump,width):
			color = promedio_para_img(i,j,i+altojump,j+anchojump,imagen)
			for x in range(i,i+altojump+1):
				for c in range(j,j+anchojump+1):
					img[x][c] = color
	return img
def moreBrightness(imagen,factor):
	height = imagen.shape[0]
	width = imagen.shape[1]
	img = np.zeros((height,width,3),dtype=int)
	for i in range(height):
		for j in range(width):
			for k in range(3):
				img[i][j][k] =imagen[i][j][k]*factor 
	return img