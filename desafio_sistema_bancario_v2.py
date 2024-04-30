def menu():
    menu = '''\n
    +++++++++++++ MENU +++++++++++++

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Cliente
    [5] Abrir Conta-Corrente
    [6] Listar Contas
    [0] sair

    Por favor, selecione uma das opções acima.
    '''
    return input(menu)



def depositar(saldo, valor, extrato, /): 
    if valor > 0:
        saldo += valor
        extrato += f"Depósito R$: {valor:.2f}\n"
        print("\n+++ Depósito realizado com sucesso! +++")
    else:
        print("\n:::: Falha na operação! Por favor, digite um valor a ser depositado. ::::")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limites = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("::::Falha na operação! Seu saldo é insuficiente para realizar esta transação.::::")

    elif excedeu_limites:
        print("::::Falha na operação! Esta transação excede o seu limite de saque.::::")

    elif excedeu_saques:
        print("::::Falha na operação! Quantidade de saques diária excedida.::::")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n+++ Saque realizado com sucesso! +++")

    else:
        print("Falha na operação! Por favor, digite um valor a ser sacado.")


def exibir_extrato(saldo, /, *, extrato):
    print("\n+++++++++++++++ EXTRATO +++++++++++++++")
    print("Não foi realizada nenhuma transação." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("+++++++++++++++++++++++++++++++++++++++")


def criar_usuario(usuarios):     
    cpf = input("Digite apenas os números do CPF (11 dígitos): ")
    usuario = filtrar_usuario(cpf, usuarios)
    

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("::::Já existe usuário cadastrado com este CPF.::::")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (Rua, Nº, Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n+++ Cliente cadastrado com sucesso! +++")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n+++ Conta-Corrente criada com sucesso! +++")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n::::Cliente não encontrado na nossa base de dados. Processo de abertura de conta encerrado.::::")


def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agencia:{conta['agencia']}   
        Conta-Corrente:{conta['numero_conta']}
        Titular:{conta['usuario']['nome']}
    '''
    print("=" * 100)
    print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios= []
    contas = []

    while True:
        opcao = menu()

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

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)


        elif opcao == "0":
            print("Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação Inválida. Por favor, selecione novamente a opção desejada.")


main()