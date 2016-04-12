# -*- coding: utf-8 -*-
import zipfile
import sys
import os
import logging


#writing a zip File
#voy a utilizar la clase de logging con sus metodos info y error
#introducción al try catch ... 
# err = sys.exc_info() retorna la info de la exeption


#creo el archivo de log
logging.basicConfig(filename = "logfile.log", level = logging.DEBUG)
# tiro el primer mensaje
logging.info("Checking if the file exist")


if os.path.exists("backup.zip"):
    logging.info("It exist")
    # intentamos generar el zipfile
    try:
        zip_file = zipfile.ZipFile("backup.zip","a")
    except:
        #toma la info de la excepción
        err = sys.exc_info()
        logging.error("error to open backup.zip in appendmoed")
        #loguea con criticidad de error - en la pos 1 del arra
        logging.error("error Num: " + str(err[1].args[0]))
        
        logging.error("Error Mesg: " + err[1].args[1])

else:
    logging.info("creating a zip file")
    try:
        zip_file = zipfile.ZipFile("backup.zip","w")
    except:
        err = sys.exc_info()
        logging.error("error to write the backup.zip")
        logging.error("error Num: " + str(err[1].args[0]))
        logging.error("Error Mesg: " + err[1].args[1])

logging.info("adding test.txt to backup.zip")

try:
    zip_file.write("test.txt","test.txt",zipfile.ZIP_DEFLATED)

except:
    err = sys.exc_info()
    logging.error("no puedo crear el zip backup.zip")
    logging.error("error Num: " + str(err[1].args[0]))
    logging.error("Error Mesg: " + err[1].args[1])


    




