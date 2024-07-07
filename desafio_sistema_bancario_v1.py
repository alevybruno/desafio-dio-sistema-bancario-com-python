menu = '''

[1] depositar
[2] sacar
[3] extrato
[0] sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$: {valor:.2f}\n"

        else:
            print("Falha na operação! Por favor, digite um valor a ser depositado.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limites = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Seu saldo é insuficiente para realizar esta transação.")

        elif excedeu_limites:
            print("Falha na operação! Esta transação excede o seu limite de saque.")

        elif excedeu_saques:
            print("Falha na operação! Quantidade de saques diária excedida.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação! Por favor, digite um valor a ser sacado.")

    elif opcao == "3":
        print("\n+++++++++++++++ EXTRATO +++++++++++++++")
        print("Não foi realizada nenhuma transação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("+++++++++++++++++++++++++++++++++++++++")

    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação Inválida. Por favor, selecione novamente a opção desejada.")

