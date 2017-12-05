from skimage import io, color, filters, morphology, exposure
import os

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

def branco (imagem):
	if (imagem[0]==1.0 and imagem[1]==1.0 and imagem[2] == 1.0):
		return True
	return False

def pegarEntrada():
	global fator
	flag = True

	while(flag):
		caminho = input('Digite o caminho da imagem:\n')
		try:
			io.imread(caminho, True)
			flag = False
			fator = int(input('Digite a cada quantos pixels pintados deseja salvar a imagem:\n'))	
		except Exception as e:
			print('\n\nErro:\n')
			print(e)
			print('\n\n')

	return caminho



imagem = io.imread(pegarEntrada(), True)

linhas, colunas = imagem.shape

limiarizar(imagem, 0.6)
imagem = morphology.erosion(imagem, morphology.square(3))
imagem = morphology.erosion(imagem, morphology.square(3))
imagem = morphology.erosion(imagem, morphology.square(3))

imagem = morphology.dilation(imagem, morphology.square(3))
imagem = morphology.dilation(imagem, morphology.square(3))

#a = morphology.dilation(a, morphology.square(3))


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
	if (indice == fator):
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