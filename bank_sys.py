menu = """\n
================ MENU ================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[0]\tSair
=> """


# Declaração de Variaveis 

saldo = 100.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
DIVISOR_VISUAL = "==="
ending_line = DIVISOR_VISUAL.center(39, "=")

# Loop while

while True:
    
    opcao = str(input(menu))

    if opcao == "1":
        print('\nDeposito')

        try:
            deposito = float(input('Digite o valor que será depositado: '))
            if deposito < 0:
                print("Digite um valor valido.")
                continue
            saldo += deposito
            extrato += f"Deposito de: R${str(deposito)}\n"

            res = input('Gostaria de ver o saldo atual da conta? [S/N]')

            if res.upper() == "S":
                print(f"O saldo é de: R${saldo:.2f}")
                    
        except ValueError:
            print("Por favor apenas valores validos.")
        

    elif opcao == "2":
        print('\nSaque')

        try:
            saque = float(input('Digite o valor que será sacado: '))
            if numero_saques < LIMITE_SAQUES:

                if saque <= 500:

                    if saldo >= saque:

                        saldo = saldo - saque
                        extrato += f"Saque de: R${str(saque)}\n"
                        numero_saques += 1

                    else:
                        print("Voce nao possui saldo suficiente.")

                else:
                    print("O valor máximo de saque é de R$500.")
                    
            else:
                print("Voce excedeu a quantidade de saques diario.")
                    
        except ValueError:
            print("Por favor apenas valores validos.")


    elif opcao == "3":
        print('\nExtrato')
        print(extrato)
        print(f'Saldo atual: R${saldo:.2f}')


    elif opcao == "0":
        print("\nObrigado por usar nossos servicos")
        break


    else:
        print("Por favor, digite apenas valores validos")

    print(ending_line)