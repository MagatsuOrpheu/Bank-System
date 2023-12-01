menu = """\n
================ MENU ================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo Usuario
[5]\tNova Conta Corrente
[0]\tSair
=> """


# Declaração de Variaveis 



# Loop while 
def main():
    saldo = 100.00
    limite = 500.00
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = '0001'
    DIVISOR_VISUAL = "==="
    ending_line = DIVISOR_VISUAL.center(39, "=")


    while True:
        opcao = str(input(menu))

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                saldo=saldo,
                extrato=extrato,
                limite=limite
            )

        elif opcao == "3":
            puxar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            usuarios = criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            agencia = AGENCIA
            conta = criar_contas(numero_conta, agencia, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "0":
            print("\nObrigado por usar nossos servicos!")
            break

        else:
            print("Por favor, digite apenas valores validos.")

        print(ending_line)


# Defs

def depositar(saldo, extrato):
    print('\nDeposito')
    valor = float(input('Digite o valor que será depositado: '))
    if valor > 0:
        saldo += valor
        extrato += f"\nDeposito: R$ {valor:.2f}"
        print("Valor Depositado!")
    else:
        print("Digite um valor valido.")
    return saldo, extrato


def sacar(*, numero_saques, limite_saques, saldo, extrato, limite):
    print('\nSaque')
    saque = float(input('Digite o valor que sera sacado: '))
    if saldo >= saque:
    
        if saque <= limite:
            
            if numero_saques < limite_saques:

                if saque > 0:
                    saldo = saldo - saque
                    extrato += f'\nSaque: R$ {saque:.2f}'
                    numero_saques = numero_saques + 1
                    print('Saque realizado!')
                else:
                    print('Digite apenas valores validos.')
            else:
                print('Voce atingiu o limite de saques diarios.')
        else:
            print('Valor de saque maximo (R$500) ultrapassado.')
    else:
        print('O valor excede o montante presente na conta')
    return saldo, extrato, numero_saques


def puxar_extrato(saldo, /, *, extrato):
    print('\nExtrato:')
    print(extrato)
    print(f'\nSaldo atual: R$ {saldo:.2f}')


def criar_usuario(usuarios):
    cpf = int(input('Digite o CPF: '))
    usuario_existente = filtrar_usuarios(cpf,usuarios)
    
    if usuario_existente:
        print('Usuario ja cadastrado!')
        return usuarios

    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Digite o endereco(logradouro, nmro - bairro, cidade/sigla estado): ')
    usuarios.append({'nome':nome, 'data de nascimento':data_nascimento,'cpf':cpf ,'endereco':endereco})
    print("\nUsuario criado com sucesso!")
    return usuarios


def filtrar_usuarios(cpf, usuarios):
    usuario_existente = [usuario for usuario in usuarios if cpf == usuario['cpf']]
    return usuario_existente
    """
    Modo alternativo
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            print('Usuario ja cadastrado')
            return True"""


def criar_contas(numero_conta, agencia, usuarios):
    cpf = int(input('Por favor informe o cpf do usuario: '))
    usuario_existente = filtrar_usuarios(cpf, usuarios)

    if usuario_existente:
        print('Conta criada com sucesso!')
        return {'Conta':numero_conta, 'Agencia': agencia, 'CPF':cpf}

    print('Usuario nao encontrado na lista cadastrada. Verifique o numero!')

main()