#Se pide resolver el mismo problema definiendo una función recursiva
def eliminaespacios(frase): #Eliminar espacios mediante recursividad
    if frase[0] == " ": #Si el primer carácter es un espacio
        return eliminaespacios(frase[1:]) #Se llama a la función con el resto de la frase
    elif frase[-1] == " ": #Si el último carácter es un espacio
        return eliminaespacios(frase[:-1]) #Se llama a la función con el resto de la frase
    elif " " in frase: #Si hay espacios en la frase
        return eliminaespacios(frase[:frase.index(" ")]) + eliminaespacios(frase[frase.index(" ")+1:]) #Se llama a la función con la parte de la frase que hay antes del espacio y la parte de la frase que hay después del espacio
    else:
        return frase #Si no hay espacios, se devuelve la frase tal cual
print("Introduzca una frase u oración") #Se pide la frase
frase = input() #Se le da valor a la variable frase para que se guarde 
print("La frase sin espacios es: ", eliminaespacios(frase)) #Se muestra la frase sin espacios



    