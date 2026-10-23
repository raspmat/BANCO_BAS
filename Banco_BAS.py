cliente = "Chat"

conta = "1-4"
moeda_do_banco = "BAS" 
saldo = 10
opcao = 0
print("Bem-vindo ao Banco BAS, ", cliente)
print("Conta: ", conta)

   
while opcao != 5:
    print("\n===== Menu =====")    
    print("1 - Saldo atual")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Extrato")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Saldo atual: ", saldo, moeda_do_banco)
    elif opcao == 2:
        deposito = int(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            print("Depósito realizado com sucesso.\n"
                  "Valor depositado: ", deposito, moeda_do_banco, "\n"
                   "Saldo atual: ", saldo,
                   moeda_do_banco, "\n",  )
        else:
            print("Valor inválido. O depósito deve ser um número positivo.")
    elif opcao == 3:
        saque = int(input("Digite o valor do saque: "))
        if saque > 0:
            if saque <= saldo:
                saldo -= saque
                print("Saque realizado com sucesso. \n"
                      f"Valor Sacado: {saque} {moeda_do_banco} \n"
                      f"Saldo atual: {saldo} {moeda_do_banco} \n")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido. O saque deve ser um número positivo.")
    elif opcao == 4:
        print("===== Extrato da conta =====")
        print("Saldo atual: ", saldo, moeda_do_banco)
        print("==============================")
    elif opcao == 5:    
        print("Obrigado por utilizar o Banco BAS. Até logo!")
    else:
        print("Opção inválida. Tente novamente.")




