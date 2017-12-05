from skimage import io
from skimage import color
from skimage import filters
from skimage import morphology

imagem = io.imread('labirintos/labirinto5x5.png', True)

linhas, colunas = imagem.shape



def limiarizar(imagem, limiar):
	global linhas
	global colunas

	for i in range(0, linhas):
		for j in range(0,colunas):
			if imagem[i][j] < limiar: imagem[i][j] = 0 
			else: imagem[i][j] = 1 




limiarizar(imagem, 0.8)
imagem = morphology.erosion(imagem)
p = filters.sobel(imagem)
p = morphology.closing(p)
#limiarizar(p, 0.37)


'''rgb_image = color.gray2rgb(imagem)

while :
	pass
'''
io.imshow_collection([imagem, p])
io.show()