print("Hola Mundo")

x = 999
y = 9
resultado = x/y

print(resultado)

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()