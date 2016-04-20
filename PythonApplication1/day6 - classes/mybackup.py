import os
import zipfile
import glob
#class mybackup(object):
class Mybackup:
    """Es una prueba de clases en python el objetivo el lograr crear un zip de un directorio  """

    def __init__(self, zipfile=None, backupdir=None):
        """ Setear las propiedades"""
        self.backupfile = zipfile
        self.dir_to_backup = backupdir
        #return super().__init__(**kwargs)

    def check_directory(self, chkdir):
        "verifica la existencia del directorio y retorna el nombre del directorio"

        if os.path.exists(chkdir):
            if os.path.isdir(chkdir):
                return chkdir


    def check_zipfile(self, chkzip):
        """
        Verifica si existe el zipfile y retorna el objeto zip
        """
        if os.path.exists(chkzip):
            return zipfile.ZipFile(chkzip, "a")
        else:
            return zipfile.ZipFile(chkzip, "w")

    def zip_directory(self):
        """
            zipea el directorio completo
        """
        for name in glob.glob(self.dir_to_backup + '/*'):
            self.backupfile.write(
                name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        self.backupfile.close()




