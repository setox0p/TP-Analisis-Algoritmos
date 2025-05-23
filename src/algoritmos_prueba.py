
from Trabajo_integrador import busqueda_lineal, busqueda_bin, busqueda_cuadratica


lista = [10, 3, 5, 20, 7]   # ejemplo de lista
objetivo = 20

print("lista original:", lista)


pos1 = busqueda_lineal(lista, objetivo)     
print("Resultado de búsqueda lineal:", pos1)


lista_ordenada = sorted(lista)      # como es binaria se debe ordenar la lista primero
pos2 = busqueda_bin(lista_ordenada, objetivo)
print("Lista ordenada para búsqueda binaria:", lista_ordenada)
print("Resultado de búsqueda binaria:", pos2)


busqueda_cuadratica = busqueda_cuadratica(lista)
print("lista ordenada con cuadrática:", busqueda_cuadratica)
