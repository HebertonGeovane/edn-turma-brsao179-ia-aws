idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade <= 12:
    print("Você é uma crinça.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")