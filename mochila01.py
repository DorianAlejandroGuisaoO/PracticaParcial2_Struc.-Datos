import requests
import pandas as pd

# Función para leer el archivo input desde github.
def leer_archivo_github(url):
    archivo = requests.get(url)  # Leer el archivo desde el repositorio como una solo cadena.

    # Convertir el texto del archivo en una lista de líneas (las líneas son los objetos).
    lineas = archivo.text.strip().split("\n")
    objetos = [] # Tupla para guardar cada uno de los objetos con sus atributos (peso y valor)

    # Por cada línea (objeto) creamos una tupla de listas, con cada lista siendo un objeto.
    for linea in lineas:
        partes = linea.split()
        objeto, peso, valor = partes[0], int(partes[1]), int(partes[2])  # Asignar atributos a la lista
        objetos.append((objeto, peso, valor)) # Agregar cada objeto a la tupla.

    return objetos

# Implementación del problema de la mochila 0/1 con tabulación
def mochila_01(objetos, W):

    n = len(objetos)  # Número de objetos

    # Crear la tabla DP con dimensiones (n+1) x (W+1), inicializada en 0.
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Llenar la tabla DP
    for i in range(1, n + 1):
        nombre, peso, valor = objetos[i - 1]  # Obtener nombre, peso y valor del objeto actual.
        for w in range(W + 1):  # Recorrer todas las capacidades posibles desde 0 hasta W.
            if peso > w:  # Si el objeto no cabe en la capacidad actual, se mantiene el valor anterior.
                dp[i][w] = dp[i - 1][w]
            else:  # Si cabe, se elige el máximo entre no tomarlo o tomarlo.
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso] + valor)

    valor_maximo = dp[n][W]  # El valor máximo se encuentra en la última celda de la tabla

    # Recuperar los objetos seleccionados.
    w = W  # Capacidad restante
    objetos_seleccionados = []  # Lista de objetos incluidos en la mochila.
    peso_usado = 0  # Peso total de los objetos seleccionados.
    for i in range(n, 0, -1):  # Recorrer la tabla en reversa para obtener los objetos seleccionados.
        if dp[i][w] != dp[i - 1][w]:  # Si el valor cambia, significa que el objeto fue seleccionado
            nombre, peso, valor = objetos[i - 1]
            objetos_seleccionados.append((nombre, peso, valor))
            w -= peso  # Reducir la capacidad restante
            peso_usado += peso  # Sumar al peso total

    objetos_seleccionados.reverse()

    return dp, valor_maximo, objetos_seleccionados, peso_usado

# Función para imprimir la tabla con los objetos y sus atributos.
def imprimir_objetos(url):
    df_tabla = pd.read_csv(url, sep=" ", names=["Objeto", "Peso", "Valor"])
    print("\nTabla de objetos utilizada:")
    return df_tabla

# Función para imprimir los resultados para cada conjunto de objetos.
def imprimir_resultados(v_max, p_usado, obj_selec):
    print("\nValor máximo posible:", v_max)
    print("Peso total usado:", p_usado)

    df_seleccionados = pd.DataFrame(obj_selec, columns=["Objeto", "Peso", "Valor"])
    print("Objetos seleccionados:")
    print(df_seleccionados.to_string(index=False))
    print("")

def menu(casos):

    for _ in range(casos):

        # Leer y guardar el archivo.
        url = input("Ingrese la URL raw de GitHub del conjunto de objetos: " + "\n")
        archivo_mochila = leer_archivo_github(url)

        capacidad_maxima = int(input("\nIngrese la capacidad máxima de la mochila: "))

        tabla_objetos = imprimir_objetos(url)
        print(tabla_objetos)

        dp, valor_maximo, objetos_seleccionados, peso_usado = mochila_01(archivo_mochila, capacidad_maxima)

        # Imprimir la tabla de DP.
        df_dp = pd.DataFrame(dp, index=["{}".format(i) for i in range(len(dp))], columns=["W_i{}".format(w) for w in range(len(dp[0]))])
        print("\nTabla DP utilizada:")
        print(df_dp.to_string(index=True))

        imprimir_resultados(valor_maximo,peso_usado,objetos_seleccionados)


print("URL EJEMPLO: https://raw.githubusercontent.com/DorianAlejandroGuisaoO/PracticaParcial2_Struc.-Datos/refs/heads/main/inputknapsack2.txt")
casos_prueba = int(input("¿Cuántos conjuntos de objetos quiere probar? " + "\n"))
menu(casos_prueba)