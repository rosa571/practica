print ("hecho por: Sanchez Juan Rosa")
def fibonacci(n):
    a, b = 0, 1
    print("Secuencia Fibonacci:")
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Introduce el número de términos de la secuencia Fibonacci: "))
fibonacci(n)