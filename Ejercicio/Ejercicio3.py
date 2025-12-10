import numpy as np
from random import randint


#Ejercicio16
'''
def da (funcion):
    def wraper (*arg,**kwargs):
        n = funcion(*arg,**kwargs)
        if type(n) == float:
              n = round(n, 2)
        return n
    return wraper

@da
def sumar (n, n2, n3):
    return ((n*n2)/n3)


print (sumar(2,4,7))

#Ejercicio17

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

#Ejercicio18

def multiplciar (uno, dos):
    return uno*dos

lista1 = [1,2,7]
lista2 = [2,4,8]

lista = list(map(multiplciar,lista1,lista2))

print(lista)

def quitarNegativo(elemento):
    return elemento >= 0

lista = [randint(-10,10) for i in range(1,6)]
print(lista)
print( list(filter(quitarNegativo, lista)))



with open('fichero.txt', 'r') as fichero:
    contenido = fichero.read().lower()

contenido = contenido.replace('á','a')
contenido = contenido.replace('é','e')
contenido = contenido.replace('í','i')
contenido = contenido.replace('ó','o')
contenido = contenido.replace('ú','u')

for c in ';:_()/%$.,':
    contenido = contenido.replace(c, '')

diccionario = {p:contenido.count(p) for p in contenido.split()}


with open('fichero.txt', 'w') as fichero:
    for valores, items in diccionario.items():
        contenido =  f"{valores}: {items} "
        fichero.write(contenido)

#print(contenido)
#print(diccionario)

print(contenido.split())


array = np.array([1,2,3,4,5,6])
print (array)
array = np.zeros((2,4), dtype=None)
print (array)
array = np.ones((4,3), dtype=None)
print (array)
array = np.full((5,1),99)
print(array)

array = np.array([1,2,3,4,5,6])
print(array)

array = array.astype(np.float32)
print(array)


#Ejercicio 9

alturas = ([180,150,179,168,190,149])


alturas = alturas [alturas > 150]

print(np.min(alturas))
print(np.max(alturas))
print(np.mean(alturas))

#Ejercicio10

alturas = np.array([180,150,179,168,190,149])


alturas = alturas [alturas > 150]

print(alturas)

#Ejercicio11

numDorsales = 15
dorsales = np.arange(1, numDorsales+1)

np.random.shuffle(dorsales)
if numDorsales %2 != 0:
    pasaDeRonda = dorsales[0] #Coge el primero
    print('Pasa a la siguiente ronda: ', pasaDeRonda)
    dorsales = dorsales[1:] #Esto transforma el array que tengo al el mismo pero desde la posicion 1, asi que se quita el 0                 
dorsales = dorsales.reshape(-1,2)
print(dorsales)

#Ejercicio13

a = np.random.normal(174,10, size=(100,))

print('Valor máximo:', np.max(a))
print('Valor mínimo:', np.min(a))
print('Media:', np.mean(a))

'''
