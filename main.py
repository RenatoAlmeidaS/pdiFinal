from skimage import io
from skimage import color
from skimage import filters
from skimage import morphology
import os

imagem = io.imread('labirintos/lab50x50.png', True)

linhas, colunas = imagem.shape



def limiarizar(imagem, limiar):
	global linhas
	global colunas

	for i in range(0, linhas):
		for j in range(0,colunas):
			if imagem[i][j] < limiar: imagem[i][j] = 0 
			else: imagem[i][j] = 1 

def encontraBranco(imagem):
	global linhas
	global colunas

	for i in range(0, linhas):
		for j in range(0,colunas):
			if imagem[i][j] == 1:
				return i, j

def desenharResposta(imagem):
	global linhas
	global colunas

def branco (imagem):
	if (imagem[0]==1.0 and imagem[1]==1.0 and imagem[2] == 1.0):
		return True
	return False

limiarizar(imagem, 0.5)
imagem = morphology.opening(imagem)

imagem = morphology.erosion(imagem)
erudita = morphology.erosion(imagem)
imagem = imagem - erudita

l,c = encontraBranco(imagem)


imagem = color.gray2rgb(imagem)
indice = 0
indicejr = 1
io.imsave('saida/image' + str(indicejr) + '.jpg', imagem)

vermelho = [1.0, 0.0, 0.0]
imagem[l][c] = vermelho
loop = True
while loop:
	indice+=1
	if (indice == 15):
		indice = 0
		indicejr+=1
		io.imsave('saida/image' + str(indicejr) + '.jpg', imagem)
	if (branco(imagem[l][c+1])):
		c+=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l+1][c])):
		l+=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l][c-1])):
		c-=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l-1][c])):
		l-=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l+1][c+1])):
		c+=1
		l+=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l-1][c+1])):
		c+=1
		l-=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l+1][c-1])):
		l+=1
		c-=1
		imagem[l][c]=vermelho
		continue
	if (branco(imagem[l-1][c-1])):
		l-=1
		c-=1
		imagem[l][c]=vermelho
		continue
	loop = False

os.system('cd saida && ffmpeg -f image2 -i image%d.jpg video.mpg && rm -r -f *.jpg')
io.imsave('saida/solucao.jpg', imagem)

io.imshow(imagem)
io.show()