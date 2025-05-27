numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Média:", round(sum(numeros)/len(numeros), 2))
print("Ordenado:", sorted(numeros))