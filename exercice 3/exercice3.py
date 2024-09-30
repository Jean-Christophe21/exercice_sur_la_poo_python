class Livre :
    def __init__(self, titre:str, auteur:str, isbn: int, statut:bool) -> None:
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = statut
    
    def emprunter(self):
        if self.disponible :
            self.disponible = False
    
    def retourner(self) :
        self.disponible = True


class Membre :
    def __init__(self, nom :str, id_membre:str, livres_empruntes : list[Livre]= []) -> None:
        self.nom = nom
        self.id_membre = id_membre
        self.livres_empruntes :list[Livre] = []
        for livre in livres_empruntes :
            """les livres emprunter ne doivent pas etre déjà preté et c'est ce qui est vérifier ici"""
            if livre.disponible == False :
                print(f"vous ne pouvez pas emprunter le livre {livre.titre} et dont l'auteur est :{livre.auteur}")
            else :
                self.livres_empruntes.append(livre)
                livre.emprunter()


    def emprunter_livres(self,livre : Livre ) :
        if livre.disponible :
            print(f"vous avez emprunter le livre :'{livre.titre}' et dont l'auteur est :{livre.auteur}")
            livre.emprunter()
            self.livres_empruntes.append(livre)
        else :
            print("le livre est indisponible pour l'instant.vous ne pouvez pas l'emprunter...")
        
    
    def retourner_livres(self, livre : Livre) :
        if livre in self.livres_empruntes :
            print(f"vous avez retourner le livre':'{livre.auteur}' de :{livre.auteur}...")
            livre.retourner()
        else : 
            print("vous ne pouvez pas retourner un livre que vous n'avez pas emprunter.")

class Bibliothèque :
    def __init__(self, nom: str, livres:list[Livre], membres: list[Membre] = []) -> None:
        self.nom = nom
        self.livres = livres
        self.membres = membres
    
    def ajouter_livres(self, livre : Livre) :
        if isinstance(livre, Livre) :
            self.livres.append(livre)
            livre.disponible = True
            print(f"vous venez d'ajouter le livre {livre.nom} a la bibliothèque.")
        else :
            print("Echec de l'ajout de livre a la bibliotheque.\nVous ne pouvez ajouter que des livres a la bibliotheque")
    
    def inscrire_membre(self,new_member: Membre) :
        if isinstance(new_member, Membre) :
            self.membres.append(new_member)
            print(f"vous venez d'ajouter {new_member.nom} à la liste des membre.")
        else :
            print("Echec de l'inscription.\nvous ne pouvez inscrire que des membres..")
    
    def lister_livres_disponible(self) :
        print("============================liste des livres disponibles===============================")
        verificateur = False
        for livre in self.livres :
            if livre.disponible :
                print(f"Nom :{livre.titre}\nAuteur :{livre.auteur}\n")
                verificateur = True

        if verificateur == False :
            print("Aucun livres n'est disponible.")    
    

    def lister_livres_empruntes(self) :
        print("============================liste des livres emprunter===============================")
        verificateur = False
        for livre in self.livres :
            if not livre.disponible :
                print(f"Nom :{livre.titre}\nAuteur :{livre.auteur}\n")
                verificateur = True

        if verificateur == False :
            print("tous les livres ont été prêtés.") 
    


l1 = Livre("un jour un soir", "anonyme", 1455, True)
l2 = Livre("voir le plus grand jour", "auteur2", 45619, True)
l3 = Livre("rire a l'aurore", "auteur3", 791791, True)
l4 = Livre("aucun_titre", "auteur4", 367175, True)
l5 = Livre("une journée", "auteur5", 141855, True)
l6 = Livre("ton amour", "auteur6", 197169, True)
l7 = Livre("un avenir", "auteur7", 1819791, True)
l8 = Livre("livre_mystere", "auteur8", 911671, True)
l9 = Livre("mythes ou realités","M_philo", 7168098, True)


list_book= [l1, l2 ,l3, l4,l5,l6,l7,l8,l9]

"""
for cpt in list_book :
    cpt.emprunter()
"""

membre1 = Membre("edouard", 917917,[l1, l4])
membre2 = Membre("augustin",1981914, [l6, l2] )
membre3 = Membre("jule",819797, [])
membre3.emprunter_livres(l5)

ma_bibliotheque = Bibliothèque("ma_biblio", list_book, [membre1, membre2])

ma_bibliotheque.inscrire_membre(membre3)  #  inscription d'un nouveau membre
ma_bibliotheque.lister_livres_disponible() 
ma_bibliotheque.lister_livres_empruntes()
membre2.retourner_livres(l2) 
membre1.emprunter_livres(l6)
ma_bibliotheque.lister_livres_disponible()
ma_bibliotheque.lister_livres_empruntes()
membre2.emprunter_livres(l2)
