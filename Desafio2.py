import textwrap

#Criação do menu
def menu():
    menu = """ \n 
    ================ Menu =============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ==>
    """
    return input(textwrap.dedent(menu))

#Função depositar
def depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo +=valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n...Depósito realizado com sucesso!...")
    else:
        print("\n Operação falhou! o valor informado é inválido.")
    return saldo, extrato

#Função sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor>saldo
    excedeu_limite = valor>limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print("\n Operação falhou! você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\n Operação falhou! o valor do saque excedeu o limite")

    elif excedeu_saques:
        print("\n Operação falhou número de saques máximo excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")

    else:
        print("\n Operação falhou! O valor informado é inválido.l")

    return saldo, extrato

#Exibir extrato
def exibir_extrato (saldo, /, *, extrato):
    print("\n =============== EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

#Criar Usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("== Usuário criado com sucesso==")

#Filtrar usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#Criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")

#Listar conta
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"][nome]}
        """
        print("="*100)
        print(textwrap.dedent(linha))



def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUE)

        elif opcao =="e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="nu":
            criar_conta(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao =="q":
            break;

        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")


main()