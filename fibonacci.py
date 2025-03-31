import time
import matplotlib.pyplot as plt

count_calls = 0
count_calls_fibonacci_simple = []
count_calls_fibonacci_memoizacion = []
count_calls_fibonacci_memoizacion_extreme = []


# Implementacion funcion de fibonacci con recursion simple
def fibonacci_simple(n):
    global count_calls  # contamos el numero de llamadas a la funcion
    count_calls += 1
    if n == 0 or n == 1:
        return n
    return fibonacci_simple(n - 2) + fibonacci_simple(n - 1)


# Implementacion funcion de fibonacci con memoizacion
def fibonacci_memoizacion(memo, n):
    global count_calls  # contamos el numero de llamadas a la funcion
    count_calls += 1
    # usamos los calculos de los sub-problemas ya resueltos para evitar redundancias
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoizacion(memo, n - 1) + fibonacci_memoizacion(memo, n - 2)

    return memo[n]


# Implementacion funcion de fibonacci con tabulacion
def fibonacci_tabulacion(n):
    if n == 1 or n == 0:
        return n
    memo = [0] * (n + 1)
    memo[1] = 1
    # Resolvemos los sub-problemas desde los mas cercanos al caso base hasta llegar al problema
    # mayor
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


# funcion para las pruebas del algoritmo con recursion simple
def pruebas_fibo_simple():
    list_n = [10, 20, 30, 35]  # valores a probar
    time_fibo_simple = []
    global count_calls
    global count_calls_fibonacci_simple
    count_calls_fibonacci_simple = []
    for i in list_n:
        count_calls = 0
        start_time = time.perf_counter()  # contamos el tiempo de ejecucion por cada valor de i
        fibonacci_simple(i)
        end_time = time.perf_counter()
        count_calls_fibonacci_simple.append(count_calls)
        time_fibo_simple.append(end_time - start_time)  # guardamos cada tiempo en una lista
    return time_fibo_simple


# Funcion para las pruebas del algoritmo con memoizacion con valores pequeños y con valores extremos
def pruebas_fibo_memoizacion(extreme_case):
    time_fibo_memoizacion = []
    list_1 = [10, 20, 30, 40]
    list_2 = [100, 250, 500, 750]
    global count_calls
    global count_calls_fibonacci_memoizacion
    global count_calls_fibonacci_memoizacion_extreme
    fibonacci_memoizacion({}, 10)  # hacemos un primer caso de prueba para calentar el cache
    # y evitar calculos de tiempo incorrectos
    if extreme_case:
        for i in list_2:
            memo = {}  # inicializamos el diccionario por cada valor de i
            count_calls = 0
            start_time = time.perf_counter()
            fibonacci_memoizacion(memo, i)
            end_time = time.perf_counter()
            count_calls_fibonacci_memoizacion_extreme.append(count_calls)
            time_fibo_memoizacion.append(end_time - start_time)  # guardamos cada tiempo en una lista
    else:
        for i in list_1:
            memo = {}
            count_calls = 0
            start_time = time.perf_counter()
            fibonacci_memoizacion(memo, i)
            end_time = time.perf_counter()
            count_calls_fibonacci_memoizacion.append(count_calls)
            time_fibo_memoizacion.append(end_time - start_time)

    return time_fibo_memoizacion


# Funcion para las pruebas del algoritmo con tabulación con valores pequeños y con valores extremos
def pruebas_fibo_tabulacion(extreme_case):
    time_fibo_tabulacion = []
    fibonacci_tabulacion(10)  # hacemos un primer caso de prueba para calentar el cache
    # y evitar calculos de tiempo incorrectos
    list_1 = [10, 20, 30, 40]
    list_2 = [100, 500, 1000, 1500]
    if extreme_case:
        for i in list_2:
            start_time = time.perf_counter()
            fibonacci_tabulacion(i)
            end_time = time.perf_counter()
            time_fibo_tabulacion.append(end_time - start_time)  # guardamos cada tiempo en una lista
    else:
        for i in list_1:
            start_time = time.perf_counter()
            fibonacci_tabulacion(i)
            end_time = time.perf_counter()
            time_fibo_tabulacion.append(end_time - start_time)
    return time_fibo_tabulacion


# ejecución de cada prueba segun corresponda
pruebas_fibo_simple = pruebas_fibo_simple()
pruebas_fibo_memoizacion_val_bajos = pruebas_fibo_memoizacion(False)
pruebas_fibo_tabulacion_val_bajos = pruebas_fibo_tabulacion(False)
pruebas_fibo_memoizacion_val_extremos = pruebas_fibo_memoizacion(True)
pruebas_fibo_tabulacion_val_extremos = pruebas_fibo_tabulacion(True)

# OUTPUT
print("Pruebas del algoritmo de fibonacci con distintos enfoques\n")
print(
    "Pruebas fibonacci con recursion simple:\nTiempos(s) para el n numero de la serie de fibonacci de la lista [10,20,30"
    ",40], respectivamente:\n", pruebas_fibo_simple, "\nNumero de llamadas a la funcion, respectivamente: ",
    count_calls_fibonacci_simple, "\n")
print("Pruebas fibonacci con memoizacion:\nTiempos(s) para el n numero de la serie de fibonacci de la lista [10,20,30"
      ",40], respectivamente:\n", pruebas_fibo_memoizacion_val_bajos, "\nNumero de llamadas a la funcion,"
                                                                      " respectivamente: ",
      count_calls_fibonacci_memoizacion, "\n")
print("Pruebas fibonacci con tabulacion:\nTiempos(s) para el n numero de la serie de fibonacci de la lista [10,20,30"
      ",40], respectivamente:\n", pruebas_fibo_tabulacion_val_bajos, "\n")
print(
    "Pruebas fibonacci con memoizacion con casos extremos:\nTiempos(s) para el n numero de la serie de fibonacci de la lista [100,250,500"
    ",750], respectivamente:\n", pruebas_fibo_memoizacion_val_extremos, "\nNumero de llamadas a la funcion"
                                                                        ", respectivamente: ",
    count_calls_fibonacci_memoizacion_extreme, "\n")
print(
    "Pruebas fibonacci con tabulacion con casos extremos:\nTiempos(s) para el n numero de la serie de fibonacci de la lista [100,500,1000"
    ",1500], respectivamente:\n", pruebas_fibo_tabulacion_val_extremos, "\n")

list_1 = [10, 20, 30, 35]
list_2_memo = [100, 250, 500, 750]
list_2 = [100, 500, 1000, 1500]

# Graficacion de tiempos de ejecucion de fibonacci con recursion simple
plt.plot(list_1, pruebas_fibo_simple, marker='o', linestyle='-', color='b', label='Tiempo de ejecucion')
plt.xlabel("Valor de n")
plt.ylabel("log10(Tiempo de ejecución)")  # graficamos el tiempo en escala logaritmica
plt.title("Tiempo de Ejecución de Fibonacci con recursion simple")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()

# Graficacion de tiempos de ejecucion de fibonacci con memoizacion con valores bajos
plt.plot(list_1, pruebas_fibo_memoizacion_val_bajos, marker='o', linestyle='-', color='r', label='Tiempo de ejecucion')
plt.xlabel("Valor de n")
plt.ylabel("log10(Tiempo de ejecución)")  # graficamos el tiempo en escala logaritmica
plt.title("Tiempo de Ejecución de Fibonacci con memoización")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()

# Graficacion de tiempos de ejecucion de fibonacci con tabulacion con valores bajos
plt.plot(list_1, pruebas_fibo_tabulacion_val_bajos, marker='o', linestyle='-', color='r', label='Tiempo de ejecucion')
plt.xlabel("Valor de n")
plt.ylabel("log10(Tiempo de ejecución)")  # graficamos el tiempo en escala logaritmica
plt.title("Tiempo de Ejecución de Fibonacci con tabulación")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()

# Graficas para los casos extremos

# Graficacion de tiempos de ejecucion de fibonacci con memoizacion con valores extremos
plt.plot(list_2_memo, pruebas_fibo_memoizacion_val_extremos, marker='o', linestyle='-', color='r',
         label='Tiempo de ejecucion')
plt.xlabel("Valor de n")
plt.ylabel("log10(Tiempo de ejecución)")  # graficamos el tiempo en escala logaritmica
plt.title("Tiempo de Ejecución de Fibonacci con memoización(valores extremos)")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()

# Graficacion de tiempos de ejecucion de fibonacci con tabulacion con valores extremos
plt.plot(list_2, pruebas_fibo_tabulacion_val_extremos, marker='o', linestyle='-', color='r',
         label='Tiempo de ejecucion')
plt.xlabel("Valor de n")
plt.ylabel("log10(Tiempo de ejecución)")  # graficamos el tiempo en escala logaritmica
plt.title("Tiempo de Ejecución de Fibonacci con tabulación(valores extremos)")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()

# Grafica de comparacion de todos los algoritmos
plt.plot(list_1, pruebas_fibo_simple, marker='o', linestyle='-', color='b', label='Recursivo simple')
plt.plot(list_1, pruebas_fibo_memoizacion_val_bajos, marker='o', linestyle='-', color='r', label='Memoización')
plt.plot(list_1, pruebas_fibo_tabulacion_val_bajos, marker='o', linestyle='-', color='g', label='Tabulación')
plt.xlabel("Valor de n")
plt.ylabel("log10(Tiempo de ejecución)")  # graficamos el tiempo en escala logaritmica
plt.title("Tiempo de Ejecución de Fibonacci con distintos enfoques")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()
