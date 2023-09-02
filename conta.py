class Conta:

    def __init__(self, numero, titular, saldo, limite):  # Função construtora
        print("Construindo objeto ... {}".format(self))
        # Atributos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

# Métodos
    def extrato(self):
        print("Saldo {} do títular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    # Valor_a_sacar recebe o valor do saque da função sacar para testar a condição de autorização
    def __saque_permitido(self, valor_a_sacar):
        valor_autorizado = self.__saldo + self.__limite
        return valor_a_sacar <= valor_autorizado  # Retorna True para a função sacar

    def sacar(self, valor):
        # Chama a função saque_permitido para validar se o valor está dentro do limite
        if (self.__saque_permitido(valor)):
            # Com o True da Função saque_permitido, vai executar o comando.
            self.__saldo -= valor
        else:
            print("O valor solicitado de {} é maior que o permitido!".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property  # Acessa o metodo diretamente sem precisar de get
    def limite(self):
        return self.__limite

    @limite.setter  # Seta um valor diretamente em limite
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():  # Permite a consulta do método sem que haja um objeto
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
