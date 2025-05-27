def executar_operacao(operacao, a, b):
    resultado = operacao(a, b)
    print(f"Resultado da operação: {resultado}")

# Novas operações
def subtrair(x, y):
    return x - y

def dividir(x, y):
    if y == 0:
        return "Não é possível dividir por zero."
    return x / y

def ao_quadrado_da_soma(x, y):
    return (x + y) ** 2

# Testando cada operação
executar_operacao(subtrair, 10, 3)         # Esperado: 7
executar_operacao(dividir, 20, 4)          # Esperado: 5.0
executar_operacao(dividir, 10, 0)          # Esperado: erro tratado
executar_operacao(ao_quadrado_da_soma, 2, 3)  # Esperado: 25