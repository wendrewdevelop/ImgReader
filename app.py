'''
Script basico utilizando OCR com python.

OCR é, basicamente, leitura de caracteres em uma imagem, mas também pode ser 
utilizado para outros fins.
'''

from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR

print( pytesseract.image_to_string( Image.open('ocr2.png') ) ) # Extraindo o texto da imagem
print( pytesseract.image_to_string( Image.open('scannedimg.png') ) ) # Extraindo o texto da imagem