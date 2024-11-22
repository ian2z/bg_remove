from rembg import remove
from PIL import Image

# pip install rembg e pip install PIL no terminal
# caminho_imagem = nome da foto (jpeg ou png), colocar foto na pasta raiz do codigo

caminhoImagem = "photo.jpg"
caminhhoImagemSemBg = "photo_sem_gb.png"
imagemArquivo = Image.open(caminhoImagem)
imagemArquivoSemBg = remove(imagemArquivo)
imagemArquivoSemBg.save(caminhhoImagemSemBg)