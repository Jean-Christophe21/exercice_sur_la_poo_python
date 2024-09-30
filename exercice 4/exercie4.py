class Pokemon :
    def __init__(self, nom :str , hp:int, atk:int) :
        self.nom :str = nom
        if hp < 0 :
            self.hp:int = hp
        if atk < 0 :
            self.atk:int = atk

    def get_nom(self) :
        return self.nom
    
    def get_hp(self) :
        return self.hp
    
    def get_atk(self) :
        return self.atk  
    
    def isdead(self) :
        return self.hp == 0
    
    def attaquer(self, p ) :
        p.hp -= self.atk
        print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {self.atk}")

        if p.hp < 0 :
            p.hp = 0

    def afficher(self):
        print(f"Nom : {self.nom}\nHealth Points: {self.hp}\nForce de base :{self.atk}")
    

class Pokemon_feu(Pokemon) :
    def __init__(self, nom: str, hp: int, atk: int):
        super().__init__(nom, hp, atk)

    def attaquer(self, p :Pokemon):
        if isinstance(p, Pokemon_plante) :
            p.hp -= 2 * self.atk
            print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {2*self.atk}")

        elif isinstance(p(Pokemon_feu, Pokemon_eau)) :
            p.hp -= 0.5 * self.atk
            print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {0.5*self.atk}")

        elif isinstance(p, Pokemon) :
            super.attaquer(p)

        if p.hp < 0 :
            p.hp = 0


class Pokemon_eau(Pokemon) :
    def __init__(self, nom: str, hp: int, atk: int):
        super().__init__(nom, hp, atk)
    
    def attaquer(self, p):
        if isinstance(p, Pokemon_feu): 
            p.hp -= 2 * self.atk
            print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {2*self.atk}")

        elif isinstance(p,(Pokemon_eau, Pokemon_plante)) :
            p.hp -= 0.5 * self.atk
            print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {0.5*self.atk}")

        elif isinstance(p, Pokemon) :
            super().attaquer(p)


class Pokemon_plante(Pokemon) :
    def __init__(self, nom: str, hp: int, atk: int):
        super().__init__(nom, hp, atk)
    
    def attaquer(self, p):
        if isinstance(p, Pokemon_feu): 
            p.hp -= 2 * self.atk
            print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {2*self.atk}")

        elif isinstance(p,(Pokemon_eau, Pokemon_plante)) :
            p.hp -= 0.5 * self.atk
            print(f"suite a l'attaque de {self.nom}, le hp de {p.nom} a ete diminue de {0.5*self.atk}")

        elif isinstance(p, Pokemon) :
            super().attaquer(p)


