import textwrap
from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []


    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod  
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        ultrapassou_saldo = valor > saldo

        if ultrapassou_saldo:
            print("Voce nao possui saldo suficiente para a operacao!")
        
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado!')
            return True

        else:
            print("Digite apenas valores validos!")

        return False 

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Valor depositado com sucesso!')
        else:
            print('Digite apenas valores validos!')
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["Tipo"] == Saque.__name__]
            )

        ultrapassou_limite = valor > self._limite
        ultrapassou_saques = numero_saques >= self._limite_saques

        if ultrapassou_limite:
            print("Voce ultrapassou o limite de saque maximo (R$ 500)!")

        elif ultrapassou_saques:
            print("Voce ultrapassou o limite diario de saques!")

        else:
            return super().sacar(valor)
        
        return False
        
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome} 
        """
       

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor
            }
        )
    

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod    
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        
        if sucesso:
            conta.historico.adicionar_transacao(self)


menu = """\n
================ MENU ================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo Usuario
[5]\tNova Conta Corrente
[6]\tListar contas
[0]\tSair
=> """


# Declaração de Variaveis 



# Loop while 
def main():
    usuarios = []
    contas = []


    while True:
        opcao = str(input(menu))

        if opcao == "1":
            depositar(usuarios)

        elif opcao == "2":
            sacar(usuarios)

        elif opcao == "3":
            puxar_extrato(usuarios)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == "0":
            print("\nObrigado por usar nossos servicos!")
            break

        else:
            print("Por favor, digite apenas valores validos.")



# Defs

def depositar(clientes):
    cpf = int(input("Digite o CPF do proprietario: "))
    cliente = filtrar_usuarios(cpf, clientes)

    if not cliente:
        print('Cliente nao encontrado!')
        return

    valor = float(input('Digite o valor que será depositado: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = int(input("Digite o CPF do proprietario: "))
    cliente = filtrar_usuarios(cpf, clientes)

    if not cliente:
        print('Cliente nao encontrado!')
        return
    
    valor = float(input('Digite o valor que sera sacado: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def puxar_extrato(clientes):
    cpf = int(input("Digite o CPF do proprietario: "))
    cliente = filtrar_usuarios(cpf, clientes)

    if not cliente:
        print('Cliente nao encontrado!')
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n==================EXTRATO===================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = 'Nenhuma movimentacao registrada'
    else:
        for transacao in transacoes:
            extrato+= f"\n{transacao['Tipo']}:\n\tR$ {transacao['Valor']:.2f}"

    print(extrato)
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("==============================================")


def criar_usuario(clientes):
    cpf = int(input('Digite o CPF: '))
    usuario_existente = filtrar_usuarios(cpf,clientes)
    
    if usuario_existente:
        print('Usuario ja cadastrado!')
        return

    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Digite o endereco(logradouro, nmro - bairro, cidade/sigla estado): ')

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\nUsuario criado com sucesso!")
    


def filtrar_usuarios(cpf, usuarios):
    usuario_existente = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuario_existente[0] if usuario_existente else None
    

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente nao possui conta!")
        return

    return cliente.contas[0]



def criar_conta(numero_conta, usuarios, contas):
    cpf = int(input('Por favor informe o cpf do usuario: '))
    usuario_existente = filtrar_usuarios(cpf, usuarios)

    if not usuario_existente:
        print('Usuario nao encontrado!')
    
    conta = ContaCorrente.nova_conta(cliente=usuario_existente, numero=numero_conta)
    contas.append(conta)
    usuario_existente.contas.append(conta)

    print("\nConta adicinada com sucesso")


def listar_contas(contas):
    for conta in contas:
        print('========================================================')
        print(textwrap.dedent(str(conta)))
              
main()