from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricaov = descricao

    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"

    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num = num
        self.nome = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor

class Pix(Pagamento):
    def __init__(self, chave: bool, banco: str, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def resumo(self):
        return "Pix aprovado! {self.banco}:{self.chave} " + super().resumo()

class Boleto(Pagamento):
    def __init__(self, cod_barras: int, vencimento: str):
        super().__init__(valor, descricao)
        self.cod_barras = cod_barras
        self.vencimento = vencimento

    def processar(self):
        if


def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())

pag: Pagamento = CartaoCredito(nome= "David", descricao="Coxinha", limite=500.00, num=123, valor=1.0)