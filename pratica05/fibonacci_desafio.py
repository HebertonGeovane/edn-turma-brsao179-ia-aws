# fibonacci_desafio.py

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Entrada do usuário
quantidade = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

print(f"\nOs {quantidade} primeiros números da sequência de Fibonacci são:")
fibonacci(quantidade)
