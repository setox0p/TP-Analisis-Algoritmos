import time, random, csv    # mido tiempo   # genera datos de prueba    # estructura de resultados
from Trabajo_integrador import busqueda_lineal, busqueda_bin, busqueda_cuadratica


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
        lista = sorted(random.sample(range(n * 10), n))  # genero lista de elemntos ordenados (n)
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

        
    with open("resultado_busq.csv", mode="w", newline = "") as arc_csv:
        escritor = csv.writer(arc_csv)
        escritor.writerow(["tamaño", " busqueda lineal", " busqueda binaria", " busqueda cuadratica"])
        escritor.writerows(resultados)
    print("Los resultados se guardan en 'resultado_busq.csv' ")
    
    
if __name__ == "__main__":
    prints_csv()
