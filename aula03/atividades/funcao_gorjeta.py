def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

# Exemplo de uso
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor, porcentagem)

print(f"A gorjeta deve ser: R$ {gorjeta:.2f}")
