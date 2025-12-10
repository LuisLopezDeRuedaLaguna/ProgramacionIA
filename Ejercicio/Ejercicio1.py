import keyword
'''

#Ejercicio 1

print(keyword.kwlist)   

#Ejercicio 2

nota = 10
nota2 = 3

print((nota+nota2)/2)

#Ejercicio 3

numero = int(input("Introduce un número para saber si es par o inpar"))

if numero % 2 == 0:
    print('Es par')
else:
    print('Es inpar')

#Ejercicio 4

a= b= c= 'Paco' 

print(a,b,c)

#Ejercicio 5

if 23 < 230:
    print('Si, es mayor')

#Ejercicio 6

nombre = input("Declare su nombre: ")
edad = input("Declare su edad: ")

print('Su nombre es: ', nombre, '\n', 'Su edad es: ', edad )

#Ejercicio8

numero = int(input('Digame un número para determinar si es positivo o negativo o 0: '))

if numero == 0:
    print('El número es 0')
elif numero > 0:
    print('El número es positivo')
elif numero < 0:
    print('El número es negativo')

#Ejercicio10

for letra in input('Especifique su nombre para su desglose: '):
    print(letra, end='.')

#Ejercicio11

apellido = input('Especifique su apellido: ')

if es_perez := 'Pérez' in apellido:
    print('Si lo contiene')


#Ejercicio12

for numero in range(-5,6):
    if numero == 5:
        print(numero**2)
    else:
        print(numero**2, end=', ')
#Ejercicio14

nota1 = float(input('Diga la nota número 1: '))
nota2 = float(input('Diga la nota número 2: '))

print('La nota con decimales: ', (nota1+nota2)/2)
print('Nota sin de cimales: ' , int((nota1+nota2)/2))


#Ejercicio16

nombre = input('Declare su nombre: ')

print('Su nombre de usuario es: ',nombre[:4]+nombre[-3:])


#Ejercicio26

nombre = input('Especifique su nombre para sacar su número de la suerte: ')
conjunto = {}
nombre = nombre.lower()

numeros = []
for letras in nombre:
    numeros.append(ord(letras) - ord('a') + 1)

conjunto = set(numeros)
print(conjunto)


#Otra forma para 26

nombre = 'Ana'
nombre = nombre.lower()

print(conjunto)

#Ejercicio 27
nombre = 'Ana'
apellido = 'Nunez'
nombre = nombre.lower()
apellido = apellido.lower()

conjuntoNombre = {ord(letras) - ord('a') + 1 for letras in nombre}

conjuntoApellido = {ord(letrasApellidos) - ord('a') + 1 for letrasApellidos in apellido}

print(conjuntoApellido.intersection(conjuntoNombre))

#Ejercicio28

platos = {'Patatas': 9, 'tequeños': 10, 'ensalada': 2, 'carne': 5} 

for puntuacion in platos:
    if platos[puntuacion] >= 5:
        print(puntuacion, platos[puntuacion])

for comida, puntuacion in platos.items():
    if puntuacion >= 5:
        print(comida, puntuacion)

#Ejercicio29


amigos = {'Pablo': 'Negro', 'Ana': 'Rosa', 'Jose': 'Azul'}

for colores in amigos:
    print(colores)

for colores in amigos:
    print(amigos[colores])

for amigo, colores in amigos.items():
        print(amigo, colores)

nombres = [nombre for nombre in amigos] #Esta línea y la de abajo son las mismas pero la de abajo es más rápida.
nombres = list(amigos)
print(nombres)

'''
#Ejercicio32


frase = 'hola hola funciona perfe aaaas'

frase = frase.lower()
palabras = frase.split()
conjunto = set(palabras)
conjunto = sorted(conjunto)

print(conjunto)

palabra = {palabra.lower() for palabra in frase.split()}
print(sorted(palabra))