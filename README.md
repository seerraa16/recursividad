# Ejercicios de recursividad
### Link del repositorio:
## 1. Búsqueda por dicotomía en una tabla ordenada
#### Se pide resolver el mismo problema definiendo una función recursiva.
## 2. Palíndromos
#### Este ejercicio trata de escribir un algoritmo el cual sea capaz de detectar un palíndromo
## 3. La bandera de Dijkstra
#### El enunciado del problema es el siguiente:

Consideramos un conjunto de n fichas de colores. Cada ficha es de un solo color. Algunas son rojas, otras verdes y otras son azules. Inicialmente, las fichas no están alineadas en orden. El problema consiste en obtener una organización de las fichas en tres series de fichas del mismo color: primero fichas rojas, luego fichas verdes y después fichas azules. Esta organización debe obtenerse mediante intercambios sucesivos, pero el color de cada ficha solo se comprueba una vez.

Hacer un algoritmo que produzca esta ordenación para un número cualquiera de fichas. 

Cada color está representado por un número cualquiera de fichas y, en particular, puede faltar un color del conjunto. El dibujo de la figura que aparece a continuación representa un conjunto de 17 fichas en las situaciones de antes y después de la ejecución del algoritmo que se ha de definir.

images/06_02.png
El conjunto por ordenar está formado por 17 fichas de las que 7 son rojas, 6 son azules y 4 son verdes. El resultado de ordenarlas reúne las 7 fichas rojas, seguidas de las 4 fichas verdes y de las 6 fichas azules. Este orden es el RVB de tres colores y no el orden decreciente de los efectivos de tres colores. Es decir, se han ordenado los colores de las fichas en el orden R, luego V y después B, y no por los números de fichas en cada subconjunto de colores.
