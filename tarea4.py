# problema 3

import numpy as np

def problema3():
    # 1. Generar los 10 puntajes (valores entre 0 y 100)
    generador = np.random.default_rng(1010)
    puntajes = np.round(generador.uniform(low=0, high=100, size=10), 2)

    print("Puntajes de amor:")
    print(puntajes)

    # 2. Crear una matriz 2-D para almacenar las diferencias absolutas
    diferencias = np.zeros((10, 10))

    # 3. Calcular las diferencias de puntajes[i] vs puntajes[j]
    for i in range(10):
        for j in range(10):
            diferencias[i][j] = abs(puntajes[i] - puntajes[j])

    print("\nMatriz de diferencias absolutas:")
    print(diferencias)

    # Mostrar mapa de calor (al final de la función)
    import matplotlib
    matplotlib.use("TkAgg")  # o prueba "Qt5Agg" si tienes Qt
    import matplotlib.pyplot as plt  # ← ESTA LÍNEA FALTABA

    plt.figure(figsize=(8, 6))
    plt.imshow(diferencias, cmap="hot", interpolation="nearest")
    plt.title("Mapa de calor de diferencias de amor")
    plt.colorbar(label="Diferencia de los puntajes (menos mejor)")
    plt.xticks(range(10), [f"P{i}" for i in range(10)])
    plt.yticks(range(10), [f"P{i}" for i in range(10)])
    plt.xlabel("Persona j")
    plt.ylabel("Persona i")
    plt.tight_layout()
    plt.show()

#if __name__ == "__main__":
    #problema3()






########## Problema 4 ##########

def problema4():
    #import numpy as np

    #simulamos calificaciones
    calificaciones = np.array([55, 70, 45, 80, 59, 61, 30, 90, 58, 100]) # se pueden modificar los valores, preferì no usa r random
    print("Calificaciones originales:")
    print(calificaciones)

    # contador de las calificaciones modificicadas
    ceros_dados = 0

    for i in range(len(calificaciones)):
        if calificaciones[i] < 60:
            calificaciones[i] = 0
            ceros_dados += 1
            if ceros_dados == 3:
                break

    print("\nCalificaciones modificadas a 0:")
    print(calificaciones)


#if __name__ == "__main__":
    #problema4()








########## Problema 5 ##########
def problema5():
# pocisiones de los peces al final de cada movimiento
    locs = np.array([
        [0,0,0],
        [1,1,2],
        [0,0,0],
        [2,1,3],
        [5,5,4],
        [5,0,0],
        [5,0,0],
        [0,0,0],
        [2,1,3],
        [1,3,1],
    ])

    # Pesos de los peces
    generador = np.random.default_rng(1010)
    pesos = generador.normal(size=10)

    print("Pesos de los peces:")
    print(pesos)

    #diccionario que almacena los pesos de los peces
    pocisiones = {}
    for i in range(10):
        pos = tuple(locs[i]) # Convierte la posición a una tupla para usarla después como clave
        peso = pesos[i]
        # seleccionar al mas pesado cuando coinciden en la misma pocision
        if pos not in pocisiones:
            pocisiones[pos] = (i, peso) #pez y peso
        else:
            _, peso_existente = pocisiones[pos]
            if peso > peso_existente:
                pocisiones[pos] = (i, peso)

    # conocer el Id del pez
    sobrevivientes = sorted([pez for pez, _ in pocisiones.values()])
    print("\nPeces sobrevivientes:", sobrevivientes)

    # mostrar también la pocision final de cada sobreviviente
    print("\nPosiciones finales de los peces sobrevivientes:")
    for pos, (pez, _) in pocisiones.items():
        print(f"Pez {pez} en posición {tuple(int(x) for x in pos)}")

#if __name__ == "__main__":
    #problema5()








########## Problema 6 ##########
def problema6():
    # Crear el arreglo 3D lleno de ceros
    datos = np.zeros((10, 10, 10), dtype=int)

    # Lista de primos menores que 10
    primos = [2, 3, 5, 7]

    # Generador aleatorio para reproducibilidad
    generador = np.random.default_rng(1010)

    # Recorrer todas las combinaciones
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i % 2 == 1 and j % 2 == 0 and k in primos:
                    # Probabilidad del 50% de colocar un 1
                    if generador.random() < 0.5:
                        datos[i, j, k] = 1

    print("Arreglo modificado aleatoriamente con 1 donde (i impar, j par, k primo):")
    #print(datos)

    # Contar cuántos unos hay
    cantidad_unos = np.sum(datos)
    print(f"\nCantidad total de unos en el arreglo: {cantidad_unos}")

    # Mostrar coordenadas donde hay un 1
    coordenadas = np.argwhere(datos == 1)
    print("\nCoordenadas donde hay un 1:")
    for coord in coordenadas:
        print(tuple(int(x) for x in coord))

if __name__ == "__main__":
    problema6()