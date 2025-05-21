# Conversor de moeda: Real para Dólar e Euro

# Valores das moedas
valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão
valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

# Exibição dos resultados
print("Valor em Reais: R$", valor_em_reais)
print("Valor em Dólares: $", round(valor_em_dolares, 2)) #round 
print("Valor em Euros: €", round(valor_em_euros, 2))