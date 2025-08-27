palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
qtd_vogais = 0
qtd_consoantes = 0

for letra in palavra:
    if letra.isalpha():
        if letra in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

print("Quantidade de vogais:", qtd_vogais)
print("Quantidade de consoantes:", qtd_consoantes)
