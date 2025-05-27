#funcao_recursiva.py

def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n - 1)

#Programa principal

num = int(input("Digite um número: "))
print(f"O fatorial é: {fatorial(num)}")