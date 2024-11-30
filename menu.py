# Definir una lista para almacenar los registros de ropa
ropa = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Agregar (Insertar / Alta) Prenda")
    print("2. Consultar (Mostrar) Ropa")
    print("3. Modificar (Editar) Ropa")
    print("4. Eliminar (Borrar) Prenda")
    print("5. Salir")

# Función para agregar un registro de ropa
def agregar_ropa():
    nombre = input("Ingrese el nombre de la prenda (ej. Camisa, Pantalón): ")
    talla = input("Ingrese la talla (ej. S, M, L, XL): ")
    color = input("Ingrese el color de la prenda: ")
    marca = input("Ingrese la marca de la prenda: ")
    modelo = input("Ingrese el modelo de la prenda: ")
    
    ropa.append({"nombre": nombre, "talla": talla, "color": color, "marca": marca, "modelo": modelo})
    print("Prenda agregada exitosamente.")

# Función para consultar (mostrar) los registros de ropa
def consultar_ropa():
    if len(ropa) == 0:
        print("No hay prendas registradas.")
    else:
        print("\nPrendas registradas:")
        for i, prenda in enumerate(ropa, 1):
            print(f"{i}. Nombre: {prenda['nombre']}, Talla: {prenda['talla']}, Color: {prenda['color']}, Marca: {prenda['marca']}, Modelo: {prenda['modelo']}")

# Función para modificar un registro de ropa
def modificar_ropa():
    consultar_ropa()  # Mostrar las prendas antes de modificar
    if len(ropa) > 0:
        try:
            indice = int(input("Seleccione el número de la prenda a modificar: ")) - 1
            if 0 <= indice < len(ropa):
                nombre = input("Nuevo nombre de la prenda: ")
                talla = input("Nueva talla: ")
                color = input("Nuevo color: ")
                marca = input("Nueva marca: ")
                modelo = input("Nuevo modelo: ")
                
                ropa[indice] = {"nombre": nombre, "talla": talla, "color": color, "marca": marca, "modelo": modelo}
                print("Prenda modificada exitosamente.")
            else:
                print("Número de prenda no válido.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Función para eliminar un registro de ropa
def eliminar_ropa():
    consultar_ropa()  # Mostrar las prendas antes de eliminar
    if len(ropa) > 0:
        try:
            indice = int(input("Seleccione el número de la prenda a eliminar: ")) - 1
            if 0 <= indice < len(ropa):
                del ropa[indice]
                print("Prenda eliminada exitosamente.")
            else:
                print("Número de prenda no válido.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Función principal del sistema
def sistema():
    # Definir una contraseña para acceder al sistema
    contrasena = "licenciado"
    
    # Solicitar la contraseña
    intentos = 3
    while intentos > 0:
        password = input("Ingrese la contraseña: ")
        if password == contrasena:
            print("Acceso concedido.")
            break
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
    
    if intentos == 0:
        print("Acceso denegado. Has agotado los intentos.")
        return  # Salir del programa si la contraseña es incorrecta
    
    # Ciclo de vida del sistema con el menú
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_ropa()
        elif opcion == "2":
            consultar_ropa()
        elif opcion == "3":
            modificar_ropa()
        elif opcion == "4":
            eliminar_ropa()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")
print("Allison marroquin zenil y Rosa Sanchez Juan")
# Ejecutar el sistema
sistema()