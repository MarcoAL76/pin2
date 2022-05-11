import os

carpeta_nombre="C:\\Users\\marco\\OneDrive\\Documents\\semestre 6\\programas\\"
carpeta_salida="C:\\Users\\marco\\OneDrive\\Documents\\semestre 6\\programas\\"
archivo_salida="Union.txt"
archivos_lista= os.listdir(carpeta_nombre)

union=""
for archivo_nombre in archivos_lista:
    archivo=open(carpeta_nombre + archivo_nombre)
    texto=archivo.read()
    archivo.close
    union+=texto

with open(carpeta_salida+archivo_salida,"w") as salida:
    salida.write(union)