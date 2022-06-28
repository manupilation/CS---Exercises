class Eletrodomestico:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__amperagem_atual_no_motor = 0

    def ligar(self, velocidade):
        self.__velocidade = velocidade
        self.__amperagem_atual_no_motor = (
            (self.__potencia / self.__voltagem) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

class Batedeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco):
        super().__init__(cor, potencia, voltagem, preco)
        self.__cor = cor
        self.__potencia = potencia
        self.preco = preco
        self.__voltagem = voltagem
        self.__ligado = False

    def __str__(self):
        return f"""
          - Cor: {self.__cor}
          - Voltagem: {self.__voltagem}
          - Preço: {self.preco}
          - Está ligada ? {"Está ligada!" if self.__ligado == True else "Está desligada!" }
        """

batedeira_sao_judas = Batedeira('Roxa', 0, 200, 50000)
print(batedeira_sao_judas)