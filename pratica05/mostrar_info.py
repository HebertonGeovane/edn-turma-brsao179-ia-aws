# Função que recebe argumentos nomeados com **kwargs
def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

# Chamando a função
mostrar_info(nome="Carlos", idade=25, cidade="Rio de Janeiro")