#Ejercicio2

'''
palabra = 'HOLA'
numero = 1

palabraencriptada = ''
for letra in palabra:
    palabraencriptada += chr(ord(letra) + numero)

print(palabraencriptada)

#Ejercicio3

saltadores = {
	"Ana": [125, 144, ], #
	"Bea": [154, 144, 143, 188, 118, 173, 187, 116],
	"Cristobal": [179, 117, 113, 177, 134],
	"Daniel": [144, 111, 173, 162],
	"Eligio": [144, 102, 160, 186, 139, 158],
	"Francisco": [109, 188, 141, 194],
	"Genaro": [144, 115, 146],
	"Helena": [170, 112, 115, 128],
	"Inés": [144, 195, 188],
	"Julia": [144, 131],
	"Kenia": [144, 190, 188],
	"Lucas": [144, 162, 120],
	"Manoli": [158, 137, 156],
	"Nobita": [112, 111, 175, 119]
}

litime_min = 170
saltadores_pasan = []

for saltador, distancia in saltadores.items():
    if max(distancia) > litime_min:
        saltadores_pasan.append(saltador)

print(saltadores_pasan)

#Ejercicio11
#Saber si dos palabras son anagramas, que tenga las mismas letas.
p1 = 'hola'
p2 = 'perro'


print(sorted(p1))
print(sorted(p2))

if sorted(p1) == sorted(p2):
    print('Son anagramas')
    
#Ejercicio5

asignaturas = {
	'Programación': (123, 21, 46, 23, 43, 13, 21),
	'Base de datos': (123, 47, 42, 21, 44, 14),
	'Matemáticas': (11, 12, 7),
	'Lengua': (42, 22, 21, 32),
	'Aplcaciones web': (13, 20, 14, 4, 46),
	'Lenguaje de marcas': (19, 46, 13, 20, 14),
	'Geografía': (48, 32, 19, 46),
	'Educación física': (13, 35, 11, 6, 27, 7),
	'Francés': (15, 34, 17, 32, 24)
}
listaAlumnos = []
for asig in asignaturas:
    alumnos = asignaturas[asig]
    for cod in alumnos:
        if cod not in listaAlumnos:
            listaAlumnos.append(cod)
print(len(listaAlumnos))


for _, alumnos in asignaturas.items():
	for cod in alumnos:
          if cod not in listaAlumnos:
              listaAlumnos.append(cod)
            
print(len(listaAlumnos))

listaAlumnos = set()

for alumnos in asignaturas.values():
    listaAlumnos.update(alumnos)

print(len(listaAlumnos))
            
#Ejercicio6

for n in range(1, 500):
	if '3' in str(n):
		print(n)
#Declara la variable que itera, despues for, despues en que itera y despues lo de haga el for
lista = [n for n in range(1,500) if '3' in str(n)]

print(lista)

#Ejercicio7

frase = 'El número 23 de la Calle 7 claveles tiene 999 escalones'

for i in frase.split():
	if i.isnumeric():
		print(i)

print([i for i in frase.split() if i.isnumeric()])


for i in frase.split():
	if i.startswith('c'):
		print(i)

print([i for i in frase.split() if i.lower.startswith('c')])


#Ejercicio8

frase = 'mi. perro, se llama mi perro'

for c in ';:_()/%$.,':
    frase = frase.replace(c, '')

diccionario = {p:frase.count(p) for p in frase.split()}
print(diccionario)
'''
import random



def juegoRol (jugadores, **kwargs):
    diccionario = dict()
    for rol in kwargs:
        diccionario.update({rol: random.sample(jugadores, kwargs[rol])})    
    return diccionario
jugadores = ['Luis','Paco','Juan','Miguel']
print(juegoRol(jugadores, magos = 2, cocineros = 2, pinche = 3))