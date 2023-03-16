#se importan las librerias necesarias para el funcionamiento del script
#para este programa se necesita tener instalado el paquete de cruptography
#este se  puede instalar con el comando pip install cryptography

import sys
from base64 import b64encode
import hashlib
import Crypto.Protocol
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2

#se crea una funcion para generar una clave para cifrar el archivo
def genera_clave():
    #se guarda la palabra secreta que ingreso el usuario en una variable
    psw = sys.argv[3]
    #se genera una cadena de bits para hacer aleatoria la llave a crear
    slt = b'\x67\x61\x72\x63\x69\x6c\x61\x7a\x6f\x20\x66\x6c\x6f\x72\x65\x73'
    #slt = b'\x9aX\x10\xa6^\x1fUVu\xc0\xa2\xc8\xff\xceOV'
    #Se genera una llave para encriptar o desencriptar
    clave = b64encode(Crypto.Protocol.KDF.PBKDF2(password=psw,salt=slt,dkLen=32,count=10000))
    #crea y se abre el archivo clave.key para escribir
    with open("clave.key","wb") as archivo_clave:
        #se escribe dentro del archivo clave.key la clave generada
        #por fernet
        archivo_clave.write(clave)
#se crea una función para leer la clave del cifrado
def cargar_clave():
    #se lee del archivo clave.key la clave del cifrado
    return open("clave.key","rb").read()

#se crea una función en la cual se va a realizar el encriptado del archivo
def encriptar(nom_archivo,clave):
    #se crea un objeto fernet con la clave recuperada del archivo
    f=Fernet(clave)
    #se abre el arcivho a cifrar en modo de lectura binaria
    with open (nom_archivo,"rb") as archivo:
        #se guarda en una variable el contenido del archivo a cifrar
        archivo_info=archivo.read()
    #se encripta la información del archivo con el metodo encrypt incluido en
    #fernet
    encriptado = f.encrypt(archivo_info)
    #se abre el archivo que se esta encriptando en modo escritura binaria
    with open(nom_archivo,"wb") as archivo:
        #se escribe dentro del archivo a cifrar el contenido que ya fue cifrado
        archivo.write(encriptado)

#se crea una funcion para realizar el desencriptado del archivo
def desencriptar(nom_archivo,clave):
    #se crea un objeto fernet con la clave recuperada del archivo clave.key
    f = Fernet(clave)
    #se abre el archivo a descifrar en modo lectura binaria
    #si la clave no es la misma que se uso para cifrar se generará una excepcion
    with open(nom_archivo,"rb") as archivo:
        #se lee el contenido del archivo a cifrar y se guarda en una variable
        archivo_info=archivo.read()
    #Se usa el metodo decrypt de fernet para desencriptar la infomación del archivo
    desencriptado = f.decrypt(archivo_info)
    #se abre el archivo a desencriptar en modo de escritura binaria
    with open(nom_archivo,"wb") as archivo:
        #se escribe dentro del archivo la información descifrada
        archivo.write(desencriptado)

#se crea una función para generar un hash del archivo a cifrar o descifrar
def hash(file):
    #Se crea un buffer de 64kb para leer por bloques 
    buf =  65536
    #se inicializa la variable donde se almacenará el hash
    md5 = hashlib.md5()
    #se abre el archivo ingresado por el usuario para obtener el hash
    with open(file, 'rb')  as f:
        #se crea un ciclo, mientras haya datos en el archivo se seguirá iterando
        while True:
            #se lee un bloque del archivo del tamaño del buffer 64kb
            data = f.read(buf)
            #si ya no hay datos leidos del archivo se termina el ciclo
            if not data:
                break
            #se actualiza el valor del hash
            md5.update(data)
    # se imprime el hash obtenido, formateado para que sea legible
    print("             HASH md5: {0}".format(md5.hexdigest()))

#ejecucion principal del sistema si el usuario ingreso "e" se procede a encriptar
if (sys.argv[1] == "e"):
    #se indica que se inica la encriptación
    print ("             Encriptacion activada!!!")
    #se llama la funcion hash con el archivo ingresado por el usuario
    #con ella se imprimirá el hash en pantalla
    hash(sys.argv[2])
    #se genera la clave para encriptar el archivo, esta clave se guarda en un 
    #archivo llamado clave.key
    genera_clave()
    #se carga la clave en una variable
    clave = cargar_clave()
    #se guarda en una variable el nombre del archivo a encriptar
    archivo = sys.argv[2]
     #se indica el nombre del archivo a encriptar
    print("             Cifrando archivo:  ",archivo)
    #se llama a la funcion de encriptado con el nombre del archivo a encriptar
    #y la clave para encriptarla
    encriptar(archivo,clave)
    #se imprime en pantalla que el archivo ya fue encriptado
    print("              Archivo encriptado")

# ejecución en caso de que el usuario ingrese "d" para desecnriptar   
if (sys.argv[1] == "d"):
    #se indica en pantalla que se comenzará a desencriptar
    print ("             Desencriptacion activada!!!")
    #se genera la clave
    genera_clave()
    #se carga la clave desde la funcion cargar_clave y se guarda en una variable  
    clave = cargar_clave ()
    #se guarda el nombre del archivo a desencriptar en una variable
    archivo = sys.argv[2]
     #se indica el nombre del archivo a desencriptar
    print("             Descifrando archivo:  ",archivo)
    #se llama a la funcion de desencriptar con el nombre del archivo y la clave
    desencriptar(archivo,clave)
    #se imprime en pantalla que el archivo fue desencriptado
    print("              Archivo desencriptado")
    #se imprime el hash del archivo desencriptado para validar que sea igual
    #que el archivo antes de encriptar
    hash(sys.argv[2])

