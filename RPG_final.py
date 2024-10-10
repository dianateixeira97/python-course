import random

# Classe base Personagem: define os atributos e métodos comuns a todos os personagens
class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida
    
    # Método para verificar se o personagem ainda está vivo
    def esta_vivo(self):
        return self.vida > 0

# Classe Heroi que herda de Personagem: representa heróis no jogo
class Heroi(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    # Método de ataque, que será implementado nas subclasses
    def atacar(self, monstro):
        pass

# Subclasse Guerreiro que herda de Heroi
class Guerreiro(Heroi):
    def atacar(self, monstro):
        # Dano aleatório causado pelo Guerreiro entre 10 e 20
        dano = random.randint(10, 20)
        print(f"O {self.nome} atacou {monstro.nome} com a espada causando {dano} de dano!")
        dano_final = monstro.defender(dano)
        monstro.vida -= dano_final

# Subclasse Mago que herda de Heroi
class Mago(Heroi):
    def atacar(self, monstro):
        # Dano aleatório causado pelo Mago entre 8 e 18
        dano = random.randint(8, 18)
        print(f"O {self.nome} atacou {monstro.nome} com uma magia de Hogwards causando {dano} de dano!")
        dano_final = monstro.defender(dano)
        monstro.vida -= dano_final

# Classe base Monstro que herda de Personagem
class Monstro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)

    # Método de defesa, que será implementado nas subclasses
    def defender(self, dano):
        pass

# Subclasse Ogre que herda de Monstro
class Ogre(Monstro):
    def defender(self, dano):
        # Defesa do ogre: reduz o dano fixo em 5 pontos
        dano_reduzido = max(dano - 5, 0)
        print(f"{self.nome} defende-se do ataque, recebendo {dano_reduzido} de dano!")
        return dano_reduzido

    def atacar(self, heroi):
        # Dano aleatório causado pelo Ogre entre 5 e 15
        dano = random.randint(5, 15)
        print(f"{self.nome} ataca {heroi.nome} causando {dano} de dano!")
        return dano

# Subclasse Dragao que herda de Monstro
class Dragao(Monstro):
    def defender(self, dano):
        # O dragão não tem defesa especial, recebe o dano total
        print(f"{self.nome} defende-se do ataque e recebe {dano} de dano!")
        return dano

# Função que gerencia a batalha entre herói e monstro
def batalha(heroi, monstro):
    print(f"Início da batalha épica entre {heroi.nome} e {monstro.nome}!")
    while heroi.esta_vivo() and monstro.esta_vivo():
        heroi.atacar(monstro)
        if monstro.esta_vivo():
            dano_ataque = monstro.atacar(heroi)
            heroi.vida -= dano_ataque
        print(f"Vida de {heroi.nome}: {heroi.vida}")
        print(f"Vida de {monstro.nome}: {monstro.vida}")
        print("-" * 30)

    if heroi.esta_vivo():
        print(f"{heroi.nome} venceste a batalha! Parabéns, campeão!")
    else:
        print(f"{monstro.nome} venceste a batalha! Boa sorte na próxima vez!")

# Função para escolher o herói e o monstro
def escolher_personagem():
    print("Bem-vindo ao mundo de batalhas épicas!")
    print("Escolhe o teu herói:")
    print("1. Guerreiro (Ragnar, o viking imbatível!)")
    print("2. Mago (Harry, the boy who lived!)")
    
    escolha_heroi = int(input("Digite 1 ou 2: "))
    
    if escolha_heroi == 1:
        heroi = Guerreiro("Ragnar")
    elif escolha_heroi == 2:
        heroi = Mago("Harry")
    else:
        print("Escolha inválida! O Guerreiro será escolhido por padrão.")
        heroi = Guerreiro("Ragnar")

    print("Escolha seu monstro:")
    print("1. Ogre (Josh, o Horripilante!)")
    print("2. Dragão (Dragão Vermelho, o Temível!)")
    
    escolha_monstro = int(input("Digite 1 ou 2: "))
    
    if escolha_monstro == 1:
        monstro = Ogre("Josh")
    elif escolha_monstro == 2:
        monstro = Dragao("Dragão Vermelho")
    else:
        print("Escolha inválida! O Ogre será escolhido por padrão.")
        monstro = Ogre("Josh")

    return heroi, monstro

# Loop para jogar várias vezes caso queira tentar outra vezz
def jogar_novamente():
    while True:
        # Escolher personagens
        heroi, monstro = escolher_personagem()
        # Iniciar a batalha
        batalha(heroi, monstro)

        # Perguntar se o jogador quer tentar outro duelo
        jogar_outro = input("Queres tentar outro duelo? (s/n): ").strip().lower()
        if jogar_outro != 's':
            print("Obrigado por jogares! Até a próxima!")
            break

# Iniciar o jogo
jogar_novamente()