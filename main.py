import time
puntaje=20
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
print("Bienvenid@ a mi trivia sobre Cultura General XD")
print("Pondremos a prueba que tanto Sabes :v")

nombre = input("Ingresa tu nombre: ")
time.sleep(1)
print("\n Hola",GREEN+nombre+RESET, "responder las siguientes preguntas escribiendo la letra de la alternativa y presione 'Enter' para enviar tu respuesta:\n")
print("\n")
time.sleep(1)
# pregunta 1
print("1)",CYAN+"Que animal es de la selva"+RESET)
time.sleep(1)
print("a)avestruz")
print("b)tucan")
print("c)pinguino ")
print("d)pangolier ")
print("\n")
respuesta_1 = input("Tu respuesta:\n")
while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_1 == "b":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2


print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
time.sleep(1)
# pregunta 2
print("\n")
print("2)",CYAN+"El lago mas grande del peru"+RESET)
time.sleep(1)
print("a)Yarinacocha")
print("b)Querococha")
print("c)Palcacocha ")
print("d)Titicaca ")
print("\n")
respuesta_2 = input("Tu respuesta:\n")
while respuesta_2 not in ("a","b","c","d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_2 == "d":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 3
print("\n")
print("3)",CYAN+"¿Cuál es el único mamífero que puede volar?"+RESET)
time.sleep(1)
print("a)Leon")
print("b)Oso")
print("c)Pavo real ")
print("d)Murcielago ")
print("\n")
respuesta_3 = input("Tu respuesta:\n")
while respuesta_3 not in ("a","b","c","d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_3 == "d":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 4
print("\n")
print("4)",CYAN+"¿Quién es el autor de “El Quijote”?"+RESET)
time.sleep(1)
print("a)Miguel de Cervantes Saavedra")
print("b)Mario Vargas Llosa")
print("c)César Vallejo")
print("d)Abelardo Sánchez León")
print("\n")
respuesta_4 = input("Tu respuesta:\n")
while respuesta_4 not in ("a","b","c","d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_4 == "a":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 5
print("\n")
print("5)",CYAN+"Quién pintó la Mona Lisa"+RESET)
time.sleep(1)
print("a)Jan Van Eyck")
print("b)Querococha")
print("c)Leonardo Da Vinci ")
print("d)Peter Paul Rubens  ")
print("\n")
respuesta_5 = input("Tu respuesta:\n")
while respuesta_5 not in ("a","b","c","d"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_5 == "c":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 6
print("\n")
print("6)",CYAN+"¿En qué país se encuentra la Torre Eiffel?"+RESET)
time.sleep(1)
print("a)Francia")
print("b)Espeña")
print("c)Perú ")
print("d)Mexico ")
print("\n")
respuesta_6 = input("Tu respuesta:\n")
while respuesta_6 not in ("a","b","c","d"):
    respuesta_6 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_6 == "a":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 7
print("\n")
print("7)",CYAN+"¿Cuál es el río más largo del mundo?"+RESET)
time.sleep(1)
print("a)Nilo")
print("b)Amazonas")
print("c)Lena ")
print("d)Rimac")
print("\n")
respuesta_7 = input("Tu respuesta:\n")
while respuesta_7 not in ("a","b","c","d"):
    respuesta_7 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_7 == "b":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 8
print("\n")
print("8)",CYAN+"¿En qué fecha se descubrió América?"+RESET)
time.sleep(1)
print("a)El 12 de octubre de 1492")
print("b)El 28 de julio 1824")
print("c)El 12 de noviembre de 1492")
print("d)El 04 de julio de 1776 ")
print("\n")
respuesta_8 = input("Tu respuesta:\n")
while respuesta_8 not in ("a","b","c","d"):
    respuesta_8 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_8 == "a":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 9
print("\n")
print("9)",CYAN+"¿Cómo se le llama al resultado de la multiplicación?"+RESET)
time.sleep(1)
print("a)Residuo")
print("b)Exponente")
print("c)Producto ")
print("d)Dividendo ")
print("\n")
respuesta_9 = input("Tu respuesta:\n")
while respuesta_9 not in ("a","b","c","d"):
    respuesta_9 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_9 == "c":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2
  
print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
# pregunta 10
print("\n")
print("10)",CYAN+"¿Cuál es la ‘capital histórica’ de Perú?"+RESET)
time.sleep(1)
print("a)Tacna")
print("b)Lima")
print("c)Juliaca ")
print("d)Cuzco ")
print("\n")
respuesta_10 = input("Tu respuesta:\n")
while respuesta_10 not in ("a","b","c","d"):
    respuesta_10 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respues: ")
if respuesta_10 == "d":
  puntaje += 0
  print (BLUE+"Muy bien",nombre, "!"+RESET)
else:
  print (RED+"Incorrecto",nombre, "!"+RESET)
  puntaje -= 2

print(GREEN+nombre+RESET, "llevas",puntaje, "puntos")
if puntaje >= 15:
  print(BLUE+"Muy bien Sabes sobre cultura XD"+RESET)
elif puntaje <= 14:
  print(YELLOW+"Necesitas saber mas sobre cultura -_-"+RESET)
elif puntaje <= 10:
  print(RED+"Sad Estudia mas y regresa T-T"+RESET)