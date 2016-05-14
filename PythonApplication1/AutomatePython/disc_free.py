import shutil

disk_c = shutil.disk_usage("C:\\")

disc_free = disk_c.free

disc_free = (((disc_free)/1024)/1024)/1024

if disc_free < 10:
    print("te queda poco espacio " + "%.2f" % round(disc_free,2) + "GB")
else:
    print("te queda espaco")
