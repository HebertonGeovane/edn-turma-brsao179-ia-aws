# Calculadora de desconto em uma loja

# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo do desconto e preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", porcentagem_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))