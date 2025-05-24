def calculadora(): #Embora ainda não tenhamos chegado no conteúdo de funções, def inicia funções. 
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida")
            
            print(f"Resultado: {resultado}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida. Tente novamente.")

calculadora()