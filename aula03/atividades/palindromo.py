def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")