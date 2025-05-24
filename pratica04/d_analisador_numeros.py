def analisador_numeros(): #Embora ainda não tenhamos chegado no conteúdo de funções, def inicia funções. 
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par.")
                pares += 1
            else:
                print(f"{numero} é ímpar.")
                impares += 1
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.")
            continue

    print(f"\nResultado final:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

analisador_numeros()