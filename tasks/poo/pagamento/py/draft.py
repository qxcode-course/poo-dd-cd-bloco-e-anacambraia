from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"

    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: str, nome_titular: str, limite: float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite = limite


    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print(f"pagamento recusado por limite insuficiente no cartao {self.numero}")
            return
        self.limite -= self.valor
        print(f"Pagamento aprovado no cartão de numero {self.numero}, com titular de nome {self.nome_titular}.")
        print(f"Limite restante: R$ {self.limite}")

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: bool, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pix aprovado usando a chave '{self.chave}' pelo banco '{self.banco}'.")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, cod_barras: int, vencimento: str):
        super().__init__(valor, descricao)
        self.cod_barras = cod_barras
        self.vencimento = vencimento

    def processar(self):
        print("Boleto gerado, aguardando pagamento...")
        print(f"Vencimento: {self.vencimento}")


def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    print(pagamento.resumo())
    pagamento.processar()


#testes

p1 = CartaoCredito(300, "Compra no mercado", "1111.2222.3333.4444", "Ana Clara", 1000)
p2 = Pix(50, "Assinatura mensal", "ana@email.com", "Nubank")
p3 = Boleto(200, "Curso online", "789456123000111222333444555", "15/12/2025")
p4 = CartaoCredito(2000, "compra de um notebook", "5555.6666.7777.8888", "Jean Oliveira", 1000)
p5 = Boleto(500, "Pagamento de energia", "123456789123456789123456789", "12/12/2012")


pagamentos = [p1, p2, p3, p4, p5]

for p in pagamentos:
    print("\n--- Processando ---")
    try:
        processar_pagamento(p)
    except Exception as erro:
        print("Erro:", erro)

