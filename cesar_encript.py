#orden del alfabeto utilizado a b c d e f g h i j k l m n o p q r s t u v w x y z   ñ
#correspondientes desplazados d e f g h i j k l m n o p q r s t u v w x y z   ñ a b c

#para encriptar se ejecuta cesar_encript.py -e "texto a cifrar"
#Para desencriptar se ejecuta cesar_encript.py -d "texto a descifrar"

#Se importan las librerias necesarias para el funcionamiento
import sys
import argparse

#se definen las opciones disponibles para la ejecución del script
# se utiliza -e para encriptar -d para desencriptar
parser = argparse.ArgumentParser()
parser.add_argument("-e","--encriptar", help="Encriptar frase")
parser.add_argument("-d","--desencriptar", help="Desencriptar frase")
args = parser.parse_args()

#se define la funcion para desencriptar un mensaje
def desencriptar():
    #Se toma el mensaje a descifrar de los argumentos de ejecución del script
    #se convierten en minúsculas ya que solo se trabaja con minusculas
    arreglo=sys.argv[2].lower()
    #se crea una variable string donde se guardara el texto descifrado
    cod=""
    #se muestra en consola el texto a desencriptar 
    print("             Desencriptando frase:",sys.argv[2].lower())
    #se inicia el ciclo en el cual se iterará en todos los elementos
    #del texto a desencriptar
    for n in arreglo:
        #cambio en el caso especial de tener z se cambia por a
        if (ord(n) == 97):
            cod+=chr(122)
        #cambio en el caso especial de tener b se cambia por espacio
        if (ord(n) == 98):
            cod+=chr(32)
        #cambio en el caso especial de tener c se cambia por ñ
        if (ord(n) == 99):
            cod+=chr(241)
        #cambio en el caso especial de tener espacio se cambia por y
        if (ord(n) == 32):
            cod+=chr(120)
        #cambio en el caso especial de tener ñ se cambia por l
        if (ord(n) == 241):
            cod+=chr(108)
        #cambio por desplazamiento de 3 a la izquierda
        if(ord(n) < 123 ):
            if(ord(n) > 99):
                cod+=chr(ord(n)-3)
    #se imprime el mensaje decodificado
    print("             El mensaje es",cod)
    return

#se crea la funcion de desencriptar
def encriptar():
    #se crea una cadena donde se guarda el texto a cifrar, se transforman en
    #minúsculas ya que el cifrado es sólo con minúsculas
    arreglo=sys.argv[2].lower()
    #se crea una cadena vacia para guardar el texto cifrado
    cod=""
    #se imprime el mensaje a cifrar
    print("             Encriptando frase:",sys.argv[2].lower())
    #se inicia un ciclo para iterar por cada elemento del texto a cifrar
    for n in arreglo:
        #cambio en el caso especial de tener x se cambia por espacio
        if (ord(n) == 120):
            cod+=chr(32)
        #cambio en el caso especial de tener espacio se cambia por b
        if (ord(n) == 32):
            cod+=chr(98)
        #cambio en el caso especial de tener ñ se cambia por c
        if (ord(n) == 241):
            cod+=chr(99)
        #cambio en el caso especial de tener y se cambia por ñ
        if (ord(n) == 121):
            cod+=chr(241)
        #cambio en el caso especial de tener z se cambia por a
        if (ord(n) == 122):
            cod+=chr(97)
        #para las letras entre 97 y 119 (entre "a" y "w" se cambia por su 
        # desplazamiento 3 posiciones a la derecha
        if(ord(n) < 120 ):
            if(ord(n) > 96):
                cod+=chr(ord(n)+3)
    #Se imprime el texto cifrado
    print("             El criptograma es",cod)

#se crea una función que valida que la cadena sólo tenga caracteres validos
#es decir, de la "a" a la "z" además de espacio y "ñ"
def validar(cadena):
    #se crea una cadena para guardar el texto a cifrar o descifrar
    cadena = cadena.lower()
    #se itera en cada elemento del texto a cifrar o descifrar
    for n in cadena:
        #si esta fuera del rango mencionado
        if (ord(n) > 122 and ord(n) < 97 ):
            #si además no es ni un espacio ni una ñ
            if (ord(n) != 32 and ord(n) != 241 ):
                #indica que hay caracteres no validos
                print("error, se ingresaron caracteres no validos")
                #se cierra el programa
                sys.exit
#ejecución principal del programa, se valida primero el texto a encriptar
#o desencriptar
validar(sys.argv[2])
#si se ingreso la opcion -e de encriptar, se indica que se comienza a 
#encriptar y se llama a la función encriptar
if args.encriptar:
   print ("             Encriptacion activada!!!")
   encriptar()
#si se ingreso -d de desencriptar, se indica que se comenzará el proceso de
#desencriptado y se llama a la función desencriptar
if args.desencriptar:
   print ("             Desencriptacion activada!!!")
   desencriptar()
