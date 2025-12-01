from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome : str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Rugido!")

    def mover(self):
        print("Andando majestoso.")

class Elefante(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Prrrrhhh!")

    def mover(self):
        print("Marchando pesadamente.")

class Cobra(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Ssssss!")

    def mover(self):
        print("Rastejando silenciosamente.")

class Cachorro(Animal):
    def __init__(self, nome :str):
        super().__init__(nome)

    def fazer_som(self):
        print("Auau!")

    def mover(self):
        print("correndo sobre 4 patas")

class Joaninha(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Pirilim!")

    def mover(self):
        print("Voando levemente.")

class Gato(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Miauuu!")

    def mover(self):
        print("Engatinhando")

class Rato(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Ririiriirir!")

    def mover(self):
        print("Andando farejando atrás de queijo.")

class Vaca(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Muuuuuuu!")

    def mover(self):
        print("Pastando sem pressa.")

class Cavalo(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Relinchadooo!")

    def mover(self):
        print("cavalgando depressa.")

class Ovelha(Animal):
    def __init__(self, nome : str):
        super().__init__(nome)

    def fazer_som(self):
        print("Beeeeee!")

    def mover(self):
        print("Fugindo do pastor.")



def apresentar(animal : Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Tipo: {type(animal).__name__}")

#testes

animais: list[Animal] = [
    Leao("Leo"),
    Cobra("Serpico"),
    Elefante("Tromba"),
    Leao("Raion"),
    Cobra("Venom"),
    Cachorro("cururu"),
    Gato("Tom"),
    Rato("Jerry"),
    Vaca("Vaca Maro"),
    Cavalo("Spirit"),
    Ovelha("Show Carneiro")
]

for animal in animais:
    apresentar(animal)

