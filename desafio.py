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
        self._historico = Historico

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
        return self.agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
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
            return True
        else:
            print('Digite apenas valores validos!')
            return False



class ContaCorrente(Conta):
    def __init__(self,numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self.historico.transacoes if transacao['tipo'] == 'Saque'
        ])

        ultrapassou_limite = valor > self.limite
        ultrapassou_saques = numero_saques >= self.limite_saques

        if ultrapassou_limite:
            print("Voce ultrapassou o limite de saque maximo (R$ 500)!")

        elif ultrapassou_saques:
            print("Voce ultrapassou o limite diario de saques!")

        else:
            return super().sacar(valor)
        
        return False
        
    def __str__(self):
        return f"""
            Agência: \t{self.agencia}
            C/C: \t{self.numero}
            Titular: {self.cliente.nome} 
        """
       

class Historico:
    def adicionar_transacao(self, transacao):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "valor": transacao.valor
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
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        
        if sucesso:
            conta.historico.adicionar_transacao(self)