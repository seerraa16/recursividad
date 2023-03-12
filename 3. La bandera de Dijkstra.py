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

