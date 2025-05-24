def idade_em_dias(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade * 365

ano = int(input("Digite o ano de nascimento: "))
dias = idade_em_dias(ano)

print(f"Você tem aproximadamente {dias} dias de vida.")