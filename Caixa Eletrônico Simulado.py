saldo = 1000  # saldo inicial
opcao = 0

while opcao != 4:
    print("\n===== MENU CAIXA ELETRÔNICO =====")
    print("1 - Ver saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Seu saldo é R$", saldo)
    elif opcao == 2:
        saque = float(input("Digite o valor para sacar: "))
        if saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso! Novo saldo:", saldo)
        else:
            print("Saldo insuficiente!")
    elif opcao == 3:
        deposito = float(input("Digite o valor para depositar: "))
        saldo += deposito
        print("Depósito realizado com sucesso! Novo saldo:", saldo)
    elif opcao == 4:
        print("Saindo... Obrigado por usar nosso banco!")
    else:
        print("Opção inválida! Tente novamente.")
