import PyPDF2
import os 

# Cria o "mesclador" de PDF
merger = PyPDF2.PdfMerger()

# Lista os arquivos dentro de uma pasta, nesse caso, a pasta "arquivos", e os organiza (sort)
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

#Cria uma condição, o arquivo só será mesclado (append) caso seja da extensão .pdf (if pdf)
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f'arquivos/{arquivo}') #Escolhe o diretório do append

 
merger.write("PDF Final.pdf")