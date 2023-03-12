#3. La bandera de Dijkstra
#colores 
R = "Rojo" 
V = "Verde"
A = "azul"
#introducimos de manera aleatoria los colores
import random
colores = [R, V, A]
random.shuffle(colores)

print ("Cuantos cuadraditos de colores quieres?")
n = int(input())
for i in range(n):
    print (colores[i % 3], end = "")
print ()

#Ordenar colores en rojo verde y azul
def ordenar_bandera(): #creamos la funcion ordenar bandera
    if colores[0] == R and colores[1] == V and colores[2] == A:
        print (ordenar_bandera)
    elif colores[0] == R and colores[1] == A and colores[2] == V:
        #Intercambiamos A y V
        colores[1] = V
        colores[2] = A
        print (ordenar_bandera)
    elif colores[0] == V and colores[1] == R and colores[2] == A:
        #Intercambiamos R y V
        colores[0] = V
        colores[1] = R
        print (ordenar_bandera)
    elif colores[0] == V and colores[1] == A and colores[2] == R:
        #Intercambiamos R y V
        colores[0] = V
        colores[1] = R
        #Intercambiamos A y V
        colores[1] = V
        colores[2] = A
        print (ordenar_bandera)
    elif colores[0] == A and colores[1] == R and colores[2] == V:
        #Intercambiamos R y A
        colores[0] = A
        colores[1] = R
        print (ordenar_bandera)
    elif colores[0] == A and colores[1] == V and colores[2] == R:
        #Intercambiamos R y A
        colores[0] = A
        colores[1] = R
        #Intercambiamos A y V
        colores[1] = V
        colores[2] = A
        print (ordenar_bandera)
    else:
        print ("La bandera ya esta ordenada")
        

