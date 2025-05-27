def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

mostrar_info(nome="Ana", idade=30, cidade="São Paulo")