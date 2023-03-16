
"""
Flores Gaspar Juan Antonio
Garcilazo Díaz José Tristán

ejercicio 2
	
	*************************Realizado en python 3.7.3***************************

	Para instalar la herramienta de paquetes de python usar el comando 
									=> sudo apt-get install python3-pip

	
	*Requiere instalar la biblioteca de Colorama, se instala con el sisguiente comando
											 => python3 -m pip install colorama
	https://pypi.org/project/colorama/

	*Requiere instalar la biblioteca de pycryptodome, se instala con el siguiente comando
											=> python3 -m pip install pycryptodome
	https://pycryptodome.readthedocs.io/en/latest/index.html

"""
from Crypto.PublicKey import RSA 						#para algoritmo de cifrado RSA
from Crypto.Random import get_random_bytes				#para generar una llave aleatoria
from Crypto.Cipher import AES, PKCS1_OAEP				#para algoritmo de cifrado AES
from Crypto.Hash import SHA256							#para calcular el hash de los archivos
from colorama import Fore, init, Style, Back, Cursor	#para cambiar de color y formato las impresiones en consola
import subprocess  										#para ejecutar comandos del sistema operativo o lanzar programas
from time import sleep									#para esperar cierto tiempo
borra=0													#contador de ayuda para borrar la pantalla una vez elegida alguna opcion

init()#iniciar colorama

def borra_pantalla():#función para limpiar la consola
	subprocess.run("clear", shell=True)
def ayuda():#se pone ayuda para el usuario del Script
	print("aqui va la ayuda")
	sleep(2)
"""
	está función comprueba que el archivo a cifrar existe
"""
def existe_archivo(nombre):
	estado=0
	try:
		archivo=open(nombre, 'r')
		archivo.close()
		estado=1
	except FileNotFoundError:
		print(Fore.RED+"\tArchivo no encontrado..!!")
		sleep(2)
	return estado
"""
	Está función se usa para leer el archivo
"""
def  lee_arch(nombre):
	with open(nombre, 'rb') as archivo:
		datos_arch=archivo.read()
	return datos_arch
"""
	Calcular hash de los archivos
"""
def archivo_hash(data):
	h = SHA256.new()
	h.update(data)
	return h.hexdigest()
"""
	gen_llaves_RSA es la función encargada de generar las llaves y dejarlas en un archivo
"""
def gen_llaves_RSA():
	key = RSA.generate(2048)
	private_key = key.export_key()
	file_out = open("private.pem", "wb")
	file_out.write(private_key)
	file_out.close()
	public_key = key.publickey().export_key()
	file_out = open("public.pem", "wb")
	file_out.write(public_key)
	file_out.close()
	print("Se están generando tus llaves...")
	sleep(4)

def cifrado_RSA():
	nombre_archivo=input("Ingrese el nombre del archivo a cifrar (con extension): ")
	if (existe_archivo(nombre_archivo)==1):
		data = lee_arch(nombre_archivo)
		hash_arc=archivo_hash(data)
		print("El hash es: ")
		print(hash_arc)
		sleep(2)
		archivo_salida=open(nombre_archivo, "wb")
		
		recipient_key = RSA.import_key(open("public.pem").read())
		session_key = get_random_bytes(16)
		# Cifre la clave de sesión con la clave pública RSA
		cipher_rsa = PKCS1_OAEP.new(recipient_key)
		enc_session_key = cipher_rsa.encrypt(session_key)

		# Cifre los datos con la clave de sesión AES
		cipher_aes = AES.new(session_key, AES.MODE_EAX)
		ciphertext, tag = cipher_aes.encrypt_and_digest(data)
		[ archivo_salida.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
		archivo_salida.close()
		print("cifrando tu archivo...")
		sleep(5)

def descifrado_RSA():
	nombre_archivo=input("Ingrese el nombre del archivo a Descifrar (con extension): ")
	if (existe_archivo(nombre_archivo)==1):
		archivo_entrada = open(nombre_archivo, "rb")
		private_key = RSA.import_key(open("private.pem").read())
		enc_session_key, nonce, tag, ciphertext = \
	   	   [ archivo_entrada.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
	   	# Descifre la clave de sesión con la clave RSA privada
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)
		# Descifre los datos con la clave de sesión AES
		cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
		data = cipher_aes.decrypt_and_verify(ciphertext, tag)
		with open(nombre_archivo,"wb") as archivo:
			archivo.write(data)
		hash_arc=archivo_hash(data)
		print("El hash es: ")
		print(hash_arc)
		sleep(2)
		print("archivo descifrado")
		sleep(5)
"""
opcion es la función encargada de llamar a las demás funciones según lo 
seleccionado por el usuario
"""
def opcion(numero):
	if numero == "1":
		gen_llaves_RSA()
	elif numero == "2":
		cifrado_RSA()
	elif numero == "3":
		descifrado_RSA()
	elif numero == "h":
		ayuda()
	else:
		print(Fore.RED+"\topcion invalida...!")
		sleep(1)
"""
control es una función que muestra las opciones a elegir,
está siempre a la espera de una opción seleccionada por el usuario
"""
def control():
	global semaforo_total, borra
	borra_pantalla()
	print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.YELLOW+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>> SCRIPT DE CIFRADO <<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>> Realizado por: <<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>> FLORES GASPAR JUAN ANTONIO <<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>> Y <<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>> Garcilazo Díaz José Tristán <<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	while True:
		if(borra != 0):
			borra_pantalla()
		print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.BLUE+"********************* OPCIONES *******************\n")
		print(" 1 => Generar llaves RSA")
		print(" 2 => Cifrado RSA")
		print(" 3 => Descifrado RSA")
		print(" h => AYUDA")
		print(" 0 => SALIR\n")
		numero=input(Fore.GREEN+" ~ $$"+Style.RESET_ALL)
		if numero== "0":
			break
		opcion(numero)
		borra+=1


control()



