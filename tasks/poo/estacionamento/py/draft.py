from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.hora_entrada = 0

    def setEntrada(self, hora):
        self.hora_entrada = hora

    def getEntrada(self):
        return self.hora_entrada

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    @abstractmethod
    def calcular_valor(self, hora_saida):
        pass

    def __str__(self):
        tipo_pad = "_" * (10 - len(self.tipo)) + self.tipo
        id_pad = "_" * (10 - len(self.id)) + self.id
        return f"{tipo_pad} : {id_pad} : {self.hora_entrada}"

class Bike(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Bike")

    def calcular_valor(self, hora_saida):
        return 3.0

class Moto(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Moto")

    def calcular_valor(self, hora_saida):
        tempo = hora_saida - self.hora_entrada
        return tempo / 20

class Carro(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Carro")

    def calcular_valor(self, hora_saida):
        tempo = hora_saida - self.hora_entrada
        valor = tempo / 10
        return 5 if valor < 5 else valor

class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.horaAtual = 0

    def procurar_veiculo(self, id):
        for i, v in enumerate(self.veiculos):
            if v.getId() == id:
                return i
        return -1
        v = self.veiculos[idx]
        valor = v.calcular_valor(self.horaAtual)

        

    def passarTempo(self, tempo):
        self.horaAtual += tempo

    def estacionar(self, veiculo) -> str:
        veiculo.setEntrada(self.horaAtual)
        self.veiculos.append(veiculo)

    def pagar(self, id ):
        idx = self.procurar_veiculo(id)
        if idx == -1:
            return

        print(
            f"{v.getTipo()} chegou {v.getEntrada()} saiu {self.horaAtual}."
            f"Pagar R$ {valor:.2f}"
        )

    def sair(self, id):
        idx = self.procurar_veiculo(id)
        if idx == -1:
            return

        self.pagar(id)
        self.veiculos.pop(idx)

    def __str__(self):
        texto = ""
        for v in self.veiculos:
            texto += str(v) + "\n"
        texto += f"Hora atual: {self.horaAtual}"
        return texto

def main():
    est = Estacionamento()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args [0] == "show":
            print(est)
        elif args [0] == "tempo":
            tempo = int(args[1])
            est.passarTempo(tempo)
        elif args[0] == "estacionar":
            tipo = args[1]
            id = args[2]

            if tipo == "bike":
                est.estacionar(Bike(id))
            elif tipo == "moto":
                est.estacionar(Moto(id))
            elif tipo == "carro":
                est.estacionar(Carro(id))
        elif args[0] == "pagar": 
            est.pagar()

                 
        

main()