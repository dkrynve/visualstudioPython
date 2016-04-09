''' Basic file operations
voy a listar los archivos de un directorio
me voy a mover entre los directorios
voy a abrir un archivo
voy a escribir un archivo
voy a leer un archivo
voy a comprobar si existe un archivo
voy a crear un directorio
voy a borrar un directorio
voy a copiar un archivo
voy a mover un archivo
voy a borrar un archivo

----
Clases y sentencias, clases os & sys & shutil
for
for anidados
if

'''
import os, sys, shutil

print ("Mi directorio actual es ... " + os.getcwd())

#esto no funciona porque retorna una lista ..... 
#print (" listo mi actual directorio" + os.listdir("."))

#esto es un ejemplo de list .----
list1 =  os.listdir(".")
for items in list1:
    print ("los items de direcrtorio son... " + os.getcwd() +  items)



list2 = os.listdir("C:\\")

for items2 in list2:
    print ("Los items del directorio son " + "C:\\" + items2)


# utiliza 3 tuplas la función os.walk para retornar. dejas el cursor arriba y vez la ayuda

for dirpath, dirname, filenames in os.walk(os.getcwd(),topdown="true"):
       for dir in dirname:
       
           for file in filenames:
               print(dirpath + "\\"+ dir +"\\" + file)


#Ahora me toca trabajar con files!!!!!!





      





