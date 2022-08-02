class Geladeira:
    def __init__(self, cor, voltagem, preco, ligada=False):
        self.cor = cor
        self.voltagem = voltagem
        self.preco = preco
        self.ligada = False

    def __str__(self):
        return f"""
          - Cor: {self.cor}
          - Voltagem: {self.voltagem}
          - Preço: {self.preco}
          - Está ligada ? {"Está ligada!" if self.ligada == True else "Está desligada!" }
        """
# uma_geladeira = Geladeira('Amarela', 220, 2500)
# print(uma_geladeira)

class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def comprar_geladeira(self, geladeira: Geladeira):
        if geladeira.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= geladeira.preco
            self.geladeira = geladeira
            print(self.saldo_na_conta)

# uma_pessoa = Pessoa("Zap Mama", 19000)
# print(uma_pessoa.comprar_geladeira(uma_geladeira))