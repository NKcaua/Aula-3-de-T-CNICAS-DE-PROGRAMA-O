contador = 0
while True:
    nome = input("Digite um nome (ou 'fim' para parar): ")
    if nome.lower() == "fim":
        break
    contador += 1
print("Quantidade de nomes digitados:", contador)
