import re

carpeta_nombre
archivo_nombre
with open(carpeta_nombre+archivo_nombre,"r")as archivo:
    texto=archivo.read()
expresion_regular=re.compile(r"")
'''

'''

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular=re.compile(r"Ni+")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado4 in resultados_busqueda
    print(resultado4.group(0))