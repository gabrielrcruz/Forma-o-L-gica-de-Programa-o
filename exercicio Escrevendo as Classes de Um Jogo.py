class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"
        
        print(f"O {self.tipo} atacou usando {ataque}")


# Exemplo de uso
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi2 = Heroi("Merlin", 150, "mago")
heroi3 = Heroi("Lee", 25, "monge")
heroi4 = Heroi("Naruto", 17, "ninja")

heroi1.atacar()  # Saída: O guerreiro atacou usando espada
heroi2.atacar()  # Saída: O mago atacou usando magia
heroi3.atacar()  # Saída: O monge atacou usando artes marciais
heroi4.atacar()  # Saída: O ninja atacou usando shuriken
