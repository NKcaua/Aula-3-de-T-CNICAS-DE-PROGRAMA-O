qtd = int(input("Quantas notas deseja inserir? "))
soma = 0
for i in range(qtd):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota
media = soma / qtd
print("A média das notas é:", media)
