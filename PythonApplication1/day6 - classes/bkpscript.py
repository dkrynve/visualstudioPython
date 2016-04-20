
from mybackup import Mybackup
import  logging
import zipfile
import os
#comienza el prog
if __name__ == "__main__":
#setea el logging
    logging.basicConfig(filename="backup.log",
                        format="%(asctime)s - %(levelname)s: %(message)s",
                        level = logging.DEBUG)

#crea el objeto backup
    logging.info("creando el objeto backup")
    bkpobj = Mybackup()
#setea el directorio a backupear
    logging.info("configurando el directorio")
    bkpobj.dir_to_backup = os.getcwd()
#set zip file
    logging.info("set the zip file")
    myzip = zipfile.ZipFile("bkp.zip" , "w")
    bkpobj.backupfile = myzip
#backup directorio    
    logging.info("backuping directory")
    bkpobj.zip_directory()
    myzip.close
