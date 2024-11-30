def generar_triangulo_pascall(filas):
    # Inicializar el triángulo con la primera fila
    triangulo = [[1]]  # La primera fila siempre es [1]
    
    # Generar el triángulo fila por fila
    for i in range(1, filas):
        fila_anterior = triangulo[i - 1]  # Obtener la fila anterior
        fila_actual = [1]  # Comenzar la nueva fila con un 1 (primera columna)

        # Generar los elementos intermedios de la fila
        for j in range(1, len(fila_anterior)):
            # Cada número es la suma de los dos números sobre él
            fila_actual.append(fila_anterior[j - 1] + fila_anterior[j])

        # Terminar la fila con un 1 (última columna)
        fila_actual.append(1)
        
        # Agregar la fila generada al triángulo
        triangulo.append(fila_actual)
    
    return triangulo

def imprimir_triangulo(triangulo):
    for fila in triangulo:
        # Imprimir cada fila de forma bonita, separando los números por espacios
        print(" ".join(map(str, fila)))

# Pedir al usuario el número de filas
filas = int(input("Introduce el número de filas del Triángulo de Pascal: "))

# Generar el Triángulo de Pascal
triangulo = generar_triangulo_pascall(filas)

# Imprimir el Triángulo de Pascal
imprimir_triangulo(triangulo)
print ("Allison marroquin zenil")