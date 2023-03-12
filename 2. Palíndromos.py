#Reconocer un palíndromo
print ("Escrba una palabra o una frase para saber si es un palindromo")
palabra = input() #pedimos que nos digan la palabra
def pasar_a_minusculas():
    palabra = palabra.lower() #pasamos la palabra a minusculas
    return palabra
def quitar_todo_tipo_de_puntosycomas(): #creamos esta funcion que lo que haces es quitar exclamaciones, interrogaciones etc
    for i in palabra:
        if i == "," or i == "." or i == " " or i == "!" or i == "?" or i == ":" or i == ";":
            palabra = palabra.replace(i, "") #reemplazamos la palabra por la palabra sin los signos de puntuacion
    return palabra
def quitar_tildes(): #En esta otra funcion, a la palabra que hemos escrito se le quitan las tildes si tiene
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    return palabra
def quitar_espacios(): #En esta funcion, a la palabra que hemos escrito se le quitan los espacios si tiene
    palabra = palabra.replace(" ", "")
    return palabra

def invertir_palabra(): #Aqui, invertimos la palabrqa que hemos escrito
    palabra_invertida = palabra[::-1]
    return palabra_invertida
palabra_invertida = invertir_palabra()
def convertir_el_palindromo(): #En esta funcion, convertimos la palabra que escribimos al principio en todas las funciones anteriores y se compara
    palabra = pasar_a_minusculas()
    palabra = quitar_todo_tipo_de_puntosycomas()
    palabra = quitar_tildes()
    palabra = quitar_espacios()
    palabra = invertir_palabra()
    return palabra
palabra = convertir_el_palindromo()
if palabra == convertir_el_palindromo: #si la palabra es igual a la palabra invertida
    print ("La palabra es un palindromo") #escribimos que es un palindromo