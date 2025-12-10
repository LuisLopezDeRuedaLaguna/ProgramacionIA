import numpy as np
from functools import reduce
#ESTRUCTURAS DE CONTROL
'''
a = 0
#If básico
if a == 0:
    print('aa')

#For básico, puedes poner, end='.' para añadirle un . al final de cada iteración
for c in "Hola":
    print(c)

#El último no se cuenta
for n in range(1, 10):
    print(n)

#El tercer número es para incrementar por ese número
for n in range(1, 10, 2):
    print(n)

#Lista
lista = ['a', 'b', 'c']
for a in lista:
    print(a)


#Enumerate, devuelve el elemento y la posición en la que se encuentra el elemento
lista = ['a', 'b', 'c']
for valor, posicion in enumerate(lista):
    print(valor, posicion)

#Zip itera dos listas al mismo tiempo, intera el número de veces de la lista mas chica, en este caso el 4 no aparece.
lista = ['a', 'b', 'c']
listaNumerica = [1, 2, 3, 4]

for letras, numeros in zip(lista, listaNumerica):
    print(letras, numeros)

#NÚMERO IMAGINARIO
#Tiene parte imaginaria y la parte real, se usan en diagramas de x e y
c = 1+2j

print(c.real)
print(c.imag)

#CADENAS

#* Hace que se repita la cadena el número de veces que se declare
a = 'Hola'
print(a* 4)

#Len longitud de la cadena
print(len(a))

#Si se ponen corchetes al lado de un string sale la letra que se declare
print(a[2]) # muestra l

#Como en el caso anterior con los corchetes y dos números se puede hacer un split, el último no se coge
a = 'Mi perro se llama paco'
print(a[3:8]) # muestra perro

#También se puede contar al reves
print(a[-1]) # muestra o

#Para buscar dentro de un string es con in
print('Pérez' in input('Especifique su apellido: '))

#Morsa, guardar el resultado de una condición directamente en una variable en la misma comprobación
apellido = input('Especifique su apellido: ')

if es_perez := 'Pérez' in apellido:
    print('Si es Pérez')
else:
    print('No es Pérez')

print(es_perez)

#Conjunto, no permiten duplicados.

conjunto = {1,2,3}

conjunto2 = set (['a', 'b', 'c'])

#Union

conjuntoTotal = conjunto | conjunto2

#Se itera como una lista

conjunto.add(1)
conjunto.remove(1) # Lo mismo pero este da una excepción si no está el elemento el otro no
conjunto.discard(1)
conjunto.pop # Quita uno aleatorio
conjunto.clear
conjunto.difference(conjunto2) #Resta, quita de los 

#Ord    

palabra = 'Ana'

ord(palabra) #Muesta letra por letra su codigo en ASCII

#Tuplas son lo mismo que una lista pero no son mutables, como las listas. Las tuplas son más rápidas de recoger que las listas por eso se usan

#Con in lo recorres normal for a in tupla
#Con enumerate para valor posicion for a, i in enumrate(tupla)
#Con zip puedes recorrer dos a la vez for t1, t2 in zip (tupla1, tupla2q)

#Diccionario


#Funciona con clave valor

diccionario = {'nombre': 'valor', 'clave': 1}

diccionario['nombre'] = 'cambiado' #Cambiar el valor de una clave

for claves in diccionario: #Muestra solo los valores
    print(claves)

for claveValor in diccionario: #Muestra valores
    print(diccionario[claveValor])

for clave, valor in diccionario.items():
    print(clave, valor)

#List compression de diccionario
#Declara la variable que itera, despues for, despues en que itera y despues lo de haga el for

numeros = [3, 7, 1, 35, 15 ,36, 1, 12301]

d = {n : n%2 == 0 for n in numeros}
print(d)

d = {n : n%2 == 0 for n in numeros if n < 100 and n != 3 } #Lo antes, pero con un if
print(d)

#Ordenar
#Se pueden ordenar palabras facilmente

palabra = 'palabra'

print(sorted(palabra))


#Funciones

def anagramas (*palabras):
    for p1 in palabras:
        for p2 in palabras:
            if sorted(p1) == sorted(p2):
                print(p1, p2, ' Son anagramas')

anagramas('japones', 'esponja')


#Update
#Mete en los set todos los elementos que le lleguen, da igual si son listas o lo que sea va a coger elemento por elemento.
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

listaAlumnos = set()

for alumnos in asignaturas.values():
    listaAlumnos.update(alumnos)
    

frase = 'El número \n sea'

print(frase)
#@Para las funciones. Esto es aplicar funciones sobre funcionaes, como por ejemplo poner una frase en mayúsculas.
 
def da (funcion):#
    def wraper (*arg,**kwargs):# Estas tres parter siempre es iguales, para guardar en n los valores que se le han pasado a sumar
        n = funcion(*arg,**kwargs)#a partir de ahí ya trabajas con los datos
        if type(n) == float:
              n = round(n, 2)
        return n
    return wraper

@da
def sumar (n, n2, n3):
    return ((n*n2)/n3)


print (sumar(2,4,7))

#Otro ejemplo

def da (funcion):
    def wraper (*arg,**kwargs):
        n = funcion(*arg,**kwargs)
        if type(n) == dict:
            n = [v for v in n.values()]
        return n
    return wraper

@da
def diccionario ():
    dc = {'nombre': 1, 'clave': 2, 1:3, 2:4}
    return dc

print(diccionario())


# Generadores
# Devuelve con yield, los variables de funcion una vez que devuelve se quedan las variables locales con sus valores.
# Si una función tiene más de un yield la primera vez que se ejecuta "acaba" en el yield, si se llama otra vez y más abajo hay
# Otro yield, sigue desde el yield anterior no desde el principio del a función, si no tiene otro si empieza desde el principio.

# Map
# Es capaz de con una lista aplicarle una funcion número por número sin tener que recorrer la lista objeto por objeto.
def cuadrado (x):
    return x**2

lista = [1,2,7]

numero = list(map(cuadrado,lista))

print(numero)


# Filtro
# Le pasas una funcion boleana y un iterable y pasa valor por valor y devuelve una lista con los que si han pasado

def divisible (numero):
    return numero %3 == 0


nu = [1,2,3,6,7,8,9]
lista = list(filter(divisible, nu))

print(lista)


#Reduce
# Va recorriendo la lista, con esto puedes hacer una función para cara iteración que haga, como se ve abajo y puedes ver la suma
# de todos los elementos o ver el más grande etc.

def max (acumulador, elemento):
    if acumulador > elemento:
        elMasgrande = acumulador
    else:
        elMasgrande = elemento
    return elMasgrande

numeros = [1,2,3,4,5]


print(reduce(max,numeros))

#Array numpy

lista = [1,2,3,4,5,6]

array = np.array(lista)

print(lista)
print(array)


#Se le pueden añadir dimensiones como se puede ver en el array de 0
array = np.zeros((2,2,2), dtype=None) #array de ceros
print(array)
array = np.ones(15, dtype=None) #array de unos
print(array)
array = np.empty(1, dtype=None) #con valores basura
print(array)
array = np.full((5,1), 10) #array relleno con valor, se le puede especificar las dimensiones entre parentesis
print(array)
array = np.arange(1,10,1) #El último no lo coge
print(array)
array = np.linspace(1,10,7) #Hace el calculo del los números del 1º al 2º usando el último. Coge del primero al último.
print(array)                #Ejemplo, el que se ve, tiene que llegar de 1 a 10 con 7 números, incrementando todos por igual
                            #En este caso incrementea de 1.5 en 1.5

array = np.zeros((10,10)) #Doble array de todos 0 de 10x10
                            
                            
#Se puede cambiar un array con astype

array = array.astype(np.float32)
array = array.astype(float) #Se puede poner tambien con tipos de py

array.ravel() #Tranforma el array en 1D

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

for i in array.ravel():
    print(i)

#Cuando a un array le aplicas una condición te devuelve otro array pero con el resultado buleano de ese array

array = np.array([1,2,-3,4,-5,6,7,-8])


resultado = array > 0
print(resultado)

#Filtrado de array, se puede filtrar de forma facil dentro de los array


alturas = np.array([180,150,179,168,190,149])


alturas = alturas [alturas > 150]

print(alturas)

#Comparar array

alturas = np.array([1,2,3,5])
alturas2 = np.array([1,2,3,4])

print((alturas == alturas2).any())
print((alturas == alturas2).all())

#Trasponer, darle la vuelta al array, las columnas son filas y las filas columnas.

a = np.array([[1,2,3,4]])

print(a)
a = a.T
print(a)

#Funciones universales de np

# Suma
a = np.array([[1,2,3,4], [5,6,7,8]])

a = a+2 #Suma 2 a todos, en forma de difusion, se aplica a todos las capas.

print(a)

#Multiplicacion

a = np.array([[1,2,3,4], [5,6,7,8]])

b = np.array([[1], [-1]])

resultado = a * b #Se adapta al ser más pequeño

#El array que multiplica tiene que ser de 1 sino da error
#a = np.array([[1,2,3,4], [5,6,7,8]])
#b = np.array([[1,2], [-1,-2]])
#Esto da error

print(resultado)

#Nampi random
#Los números random funcionan por semillas si se usa la misma se puede saber que número que va a salir

#Barajar

a = np.array([1,2,3,4,5,6,7,8,9,10])
np.random.shuffle(a)

print(a)


#Crear array

a = np.random.rand(2,3) #Sale dandon entre 0 incluido y 1 sin incluir

print(a)
a = np.random.randint(100, size = (2,3)) #Un array 2,3 y desde 0 a 100 sin incluir el 100

print(a)
'''

#Random Media

a = np.random.normal(174,20, size=(20,)) #El 20 es la desviación es como de ancho va a ser la campana, el primero es la media

print(a)

#List compression directamente en el codigo no hace falta de meterlo en una lista.
[print(round(x, 3)) for x in a]




