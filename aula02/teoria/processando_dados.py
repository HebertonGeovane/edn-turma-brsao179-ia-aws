numero = input("Digite o número: ")                      #captura número como string 
numero = float(numero)                                   #converte para float
dobro = numero * 2                                       #calcula o dobro
print("O dobro de", numero ,"é", dobro)

#Exemplo completo de Entardada de dados 
nome =  input("Digite seu nome: ")                       #captura nome do usuário
idade = int(input("Digite sua idade: "))                 #captura e converte idade
altura = float(input("Digite sua altura em metros: "))   #captura e converte altura

print("\nResumo de suas informações: ")
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros" )