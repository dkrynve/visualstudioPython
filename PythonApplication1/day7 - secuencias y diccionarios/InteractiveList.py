# Secuencias - es el paso a paso
# Diferencias entre listas y tuplas ... 
# Las listas pueden ser modificadas y las tuplas no.
my_list = ["auto","nave","avion","moto"]
print(my_list)

#desplaza el ultimo
my_list.pop()

print(my_list)

#insercion
my_list.insert(0,"moto")


print(my_list)


#rango

my_list[1:2]

# if 

if "auto" in my_list:
    print("Si esta")

#reverso
my_list.reverse()


print(my_list)


# tuplas

miTupla = ("1","2","3")
mitupla1 = ("4", "5" , "6")

miNuevaTupla = miTupla + mitupla1

print(miNuevaTupla)


#rangos

miRango = list(range(0,10,1))

print(miRango)


