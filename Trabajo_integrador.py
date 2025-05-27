import time, random, csv    # mido tiempo   # genera datos de prueba    # estructura de resultados

# Algoritmos

def busqueda_lineal(lista, objetivo):   # recorre la lista de izq a der. buscando (objetivo), si lo encuentra muestra el indice de lo contrario -1
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1


def busqueda_bin(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def busqueda_cuadratica(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# Ejemplo básico

lista = [10, 3, 5, 20, 7]   # ejemplo de lista
objetivo = 20

print("lista original:", lista)

pos1 = busqueda_lineal(lista, objetivo)     
print("Resultado de búsqueda lineal:", pos1)

lista_ordenada = sorted(lista)      # como es binaria se debe ordenar la lista primero
pos2 = busqueda_bin(lista_ordenada, objetivo)
print("Lista ordenada para búsqueda binaria:", lista_ordenada)
print("Resultado de búsqueda binaria:", pos2)

lista_cuadratica = busqueda_cuadratica(lista)
print("lista ordenada con cuadrática:", lista_cuadratica)


# Mediciones de tiempo

def medic_tiem_busq(funcion, lista, objetivo):      # mide el tiempo que demora en ejecutar una func. de busqueda
    inic = time.perf_counter()
    funcion(lista, objetivo)
    fin = time.perf_counter()
    return fin - inic


def medic_tiem_cuadr(funcion, lista):
    lista_c = lista.copy()
    inic = time.perf_counter()
    funcion(lista_c)
    fin = time.perf_counter()
    return fin - inic


def prints_csv():
    tamaño = [100, 500, 1000, 2000]
    resultados = []
    
    for n in tamaño:
        lista = sorted(random.sample(range(n * 10), n))  # genero lista de elementos ordenados (n)
        objetivo = lista[-1] 

        t1 = medic_tiem_busq(busqueda_lineal, lista, objetivo)
        t2 = medic_tiem_busq(busqueda_bin, lista, objetivo)
        t3 = medic_tiem_cuadr(busqueda_cuadratica, lista)

        print(f"tamaño : {n}")
        print(f"busqueda lineal: {t1:.6f} s")
        print(f"busqueda binaria: {t2:.6f} s")
        print(f"busqueda cuadrática: {t3:.6f} s")
        
        resultados.append([
            n,
            f"{t1:.8f}",
            f"{t2:.8f}",
            f"{t3:.8f}"
        ])

    with open("resultado_busq.csv", mode="w", newline="") as arc_csv:
        escritor = csv.writer(arc_csv)
        escritor.writerow(["tamaño", " busqueda lineal", " busqueda binaria", " busqueda cuadratica"])
        escritor.writerows(resultados)
    print("Los resultados se guardan en 'resultado_busq.csv' ")
    

if __name__ == "__main__":
    prints_csv()
