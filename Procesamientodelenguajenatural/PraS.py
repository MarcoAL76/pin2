import nltk

carpeta_nombre="C:\\Users\\marco\\OneDrive\\Documents\\semestre6\\Procesamientodelenguajenatural\\"
archivo_nombre="Arfinal.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")

#Distancia
for token in tokens:
    print(token)
palabras_total=len(tokens)
print("\nPalabras totales: ",palabras_total)

#separar palabras de 1 sola vez
tokens_conjuntos=set(tokens)
palabras_diferentes=len(tokens_conjuntos)
print("\n",tokens_conjuntos)
print("\nPalabras diferentes: ",palabras_diferentes)

#Riqueza lexica
riqueza_lexica=palabras_diferentes/palabras_total
print("\nRiqueza lexica: ",riqueza_lexica)

riqueza_lexicap=100*palabras_diferentes/palabras_total
print("\nRiqueza lexica: ",riqueza_lexicap,"%\n")

#text y concordance
texto_nltk=nltk.Text(tokens)
palabra=input("Escribe la palabra a buscar: ")
texto_nltk.concordance(palabra)
print("-----------------------------------")
texto_nltk.similar(palabra)
print("-----------------------------------")
conteo_individual=tokens.count(palabra)
print("{}".format(palabra)," se encuentra","{}".format(conteo_individual),"veces  en el texto.")