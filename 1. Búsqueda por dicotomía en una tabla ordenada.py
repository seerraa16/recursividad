#Crear una tabla de 10 elementos ordenados y buscar un numero entre ellos 
#utilizando el metodo de la busqueda por dicotomia
print ("Escriba 10 numeros ordenados de menor a mayor")
tabla = []
for i in range(10):
    tabla.append(int(input("Escriba un numero: ")))
print ("La tabla es: ", tabla)
num = int(input("Escriba el numero que desea buscar: "))
#Busqueda por dicotomia
izq = 0
der = 9
centro = 0
while (izq <= der):
    centro = (izq + der) // 2
    if (tabla[centro] == num):
        print ("El numero se encuentra en la posicion: ", centro)
        break
    elif (tabla[centro] < num):
        izq = centro + 1
    else:
        der = centro - 1
if (izq > der):
    print ("El numero no se encuentra en la tabla")
    
