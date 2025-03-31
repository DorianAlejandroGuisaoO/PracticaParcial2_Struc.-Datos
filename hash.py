# Clase para tabla hash
class hash:
    def __init__(self, size):  # constructor
        self.size = size
        self.array = [[] for _ in range(self.size)]  # creamos una lista de listas para el encadenamiento

    # Funcion para insertar clave
    def insert_key(self, keys):
        keys_list = keys.split()  # debido a que ingresa un string con posibles varias claves, las guardamos
        # en una lista
        for key in keys_list:
            index = self.hash_function(key)
            if key not in self.array[index]:  # verificamos que no se haya agregado anteriormente
                self.array[index].append(key)
                print("\nClave", key, "agregada correctamente")
            else:
                print("\nLa clave", key, "ya se encuentra en la tabla")

    # funcion hash
    def hash_function(self, key):
        sum = 0
        for i in key:
            sum += int(i)  # suma los digitos
        hash_value = sum % self.size  # modulo de la suma de digitos
        return hash_value

    # funcion para buscar una clave
    def search_key(self, keys):
        keys = keys.split()
        for key in keys:
            index = self.hash_function(key)
            if key in self.array[index]:
                print("\nLa clave", key, "esta en la tabla, en la posición ", index)
            else:
                print("\nLa clave", key, "no se encuentra en la tabla")

    def delete_key(self, keys):
        keys = keys.split()
        for key in keys:
            index = self.hash_function(key)
            if key in self.array[index]:
                index_sublist = self.array[index].index(key)
                self.array[index].pop(index_sublist)  # la eliminamos de la sublista dentro de la lista principal
                print("\nClave", key, "eliminada correctamente")
            else:
                print("\nNo fue posible borrar la clave", key)

    # funcion para imprimir la tabla
    def print_table(self):
        print("index:     keys:")
        index = 0
        for i in self.array:
            print(index, "        ", i)
            index += 1


# OUPUT
print("Tabla Hash\nEscribir el tamaño de la tabla:")
size = int(input())
hash_table = hash(size)
# creamos un menu para poder ingresar datos por consola
while True:
    print("\nMenu:\n1. Insertar claves\n2. Eliminar Clave\n3. Buscar clave\n4. Imprimir tabla\n5. Salir")
    choice = int(input())
    if choice == 1:
        print("Escriba las claves a insertar separadas por espacio: \nEjemplo: 5 10 15 20")
        clave = input("Claves: ")
        hash_table.insert_key(clave)
    elif choice == 2:
        print("Escriba las claves a eliminar separadas por espacio: \nEjemplo: 5 10 15 20")
        clave = input("Claves: ")
        hash_table.delete_key(clave)
    elif choice == 3:
        print("Escriba las claves a buscar separadas por espacio: \nEjemplo: 5 10 15 20")
        clave = input("Claves: ")
        hash_table.search_key(clave)
    elif choice == 4:
        hash_table.print_table()
    elif choice == 5:
        break
    else:
        print("\nIngrese una opción valida")
