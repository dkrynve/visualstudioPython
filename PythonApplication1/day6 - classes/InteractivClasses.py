###############es para realizar de modo interactivo.######################
#importa el modulo os
import os

#instancia con el constructor la clase mybackup

from mybackup import Mybackup

# construye el objeto
bkup = Mybackup()

#list los atributos y metodos de la clase

dir(bkup)

#pregunto por el atributo class

bkup.__class__

#pregunto que clase de cosa es ...

print (bkup.check_directory.__class__)

# pregunto por la documentacion de la clase

bkup.__doc__



#seteo la propiedad
temp = bkup.check_directory(os.getcwd())

print(temp)


