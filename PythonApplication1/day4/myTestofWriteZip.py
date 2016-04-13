# -*- coding: utf-8 -*-
import zipfile
import sys
import os
import logging
import random
#creo el archivo de log
if os.path.exists("logfile.log"):
    try:
        #rompiendo el codigo aproposito para ver el try except.
        os.remove("1logfile.log")
        
    except:
        logging.basicConfig(filename = "logfile2.log", level = logging.DEBUG)
        logging.info("Checking if the file exist")
        err = sys.exc_info()
        print("error Num: " + str(err[1].args[0]))
        print("Error Mesg: " + err[1].args[1])
        logging.error("error Num: " + str(err[1].args[0]))
        logging.error("Error Mesg: " + err[1].args[1])
        sys.exit()

logging.basicConfig(filename = "logfile.log", level = logging.DEBUG)


i =0
for i in range(10) :
    ran = random.randint(1, 10)
    if ran >= 5:
        logging.error("Es mayor")
    else:
        logging.warning("Es menor")



