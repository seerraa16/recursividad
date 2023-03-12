#Crear una tabla de 10 elementos ordenados y buscar un numero entre ellos 
#utilizando el metodo de la busqueda por dicotomia
print ("Escriba 10 numeros ordenados de menor a mayor") #decimos lo que queremos que salga por pantalla
tabla = [] #creamos la variable tabla 
for i in range(10): #hacemos que la tabloa tenga 10 numeros 
    tabla.append(int(input("Escriba un numero: "))) #vamos mostrando por pantalla escriba un numero hasta que ya se hayan escrito 10
print ("La tabla es: ", tabla) #escribimos la tabla
num = int(input("Escriba el numero que desea buscar: ")) #pedimos que nos digan el numero a buscar 
#Busqueda por dicotomia
izq = 0 #creamos la variable izq y la igualamos a 0
der = 9 #creamos la variable der y la igualamos a 9
centro = 0 
while (izq <= der): #mientras izq sea menor o igual que der
    centro = (izq + der) // 2 #centro es igual a izq mas der entre 2
    if (tabla[centro] == num): #si la tabla en la posicion centro es igual a num
        print ("El numero se encuentra en la posicion: ", centro)
        break # si es asi, se acaba el buclee 
    elif (tabla[centro] < num): #si no, si la tabla en la posicion centro es menor que num
        izq = centro + 1 #izq es igual a centro mas 1
    else:
        der = centro - 1
if (izq > der): #si izq es mayor que der
    print ("El numero no se encuentra en la tabla") # diremos que el numero no esta en la tabla ya que es imposible

