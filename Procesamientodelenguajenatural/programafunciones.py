import nltk

nltk.download('stopwords')

carpeta_nombre="C:\\Users\\marco\\OneDrive\\Documents\\semestre6\\Procesamientodelenguajenatural\\"
archivo_nombre="Arfinal.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")

texto_nltk=nltk.Text(tokens)
palabra=input("Escribe la palabra a buscar: ")

from nltk.corpus import stopwords
print(set(stopwords.words('English')))
print() 

distri=nltk.FreqDist(texto_nltk)
distri.plot(20)
print("Funcion de mas comunes en base a freqdist\n")
cant=distri.most_common() 
print(cant)
