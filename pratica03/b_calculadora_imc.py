peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc =  peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao =  "Sobrepeso"
else:
    classificacao = "Obeso"

print (f"Seu IMC é {imc:.1f}")
print(f"classificação: {classificacao}")