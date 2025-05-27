def executar_operacao(operacao, a, b):
    resultado = operacao(a, b)
    print(f"Resulatdo da operacao: {resultado}")

def soma(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

#Testes
executar_operacao(soma, 10, 5)
executar_operacao(multiplicar, 4, 3)
