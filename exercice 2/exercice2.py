from random import randint

class Employes :
    matriculeUtilisé = []    # liste contenant tous les matricules utilisées
    val_salaire = 500        # valeur du salaire
    liste_Employe = []       # liste renfermant tous les objets de types employé créé
    nbr_employe = 0          # nombre d'employé créé (ne compte pas le nombre d'instances créés pour des classes qui hérite de Employe )
    indice_salaire = 1      # cet indice 
    def __init__(self, nom : str) :
        self.nom = nom
        self.indice_salaire = Employes.indice_salaire
        self.matricule = Employes.generate_unique_matricule()      #initialisation du matricule
        if not isinstance(self, (Responsable_hierarchique, Commerciaux)):    # verifie si l'instance qui fait appel au constructeur est uniquement de type Employes
            Employes.liste_Employe.append(self)
            Employes.nbr_employe += 1


    @staticmethod
    def generate_unique_matricule()->int :  
        """cette fonction se charge de générer un numero matricule unique"""
        nbrAléatoire = randint(0, 1000000000)
        while nbrAléatoire in Employes.matriculeUtilisé :
            nbrAléatoire = randint(0, 1000000000)

        Employes.matriculeUtilisé.append(nbrAléatoire)
        return nbrAléatoire

    def affichage_caractéristique(self):
        """methode permettant d'afficher les caractéristiques d'un employé"""
        return f"Nom: {self.nom}\nindice_salaire: {self.indice_salaire}\nMatricule: {self.matricule}"

    def calcul_salaire(self) :
        """methode permettant de calculer le salaire"""
        if Employes.val_salaire <= 0 :
            return 0 
        else :
            return self.indice_salaire * Employes.val_salaire

#-----------------------------------------------------------------------------------------------------------------------------------

class Responsable_hierarchique(Employes) :
    nbr_responsable = 0           # nombre de responsable créé
    def __init__(self, nom: str):
        super().__init__(nom)
        Responsable_hierarchique.nbr_responsable += 1

    def show_inferieur_hierarchique(self) :
        for cpt in range(Employes.liste_Employe) :     
            print(Employes.liste_Employe[cpt].nom) # on affiche le nom uniquement des employés qui ont été instancié

#-----------------------------------------------------------------------------------------------------------------------------------

class Commerciaux(Employes) :
    nbr_Commerciaux = 0        # le nombre de commerciaux instancié
    ventes = 0
    def __init__(self, nom: str, ventes : int = 0 ):
        super().__init__(nom)
        self.ventes = ventes
        Commerciaux.ventes = ventes
        Commerciaux.nbr_Commerciaux += 1

    def mise_a_jour_info_ventes(self, ventes : int = 0 ) :

        if ventes < 0 :
            self.ventes = 0 
            Commerciaux.ventes = ventes
        else :
            self.ventes = ventes
            Commerciaux.ventes = ventes

    def calcul_salaire(self):
        return Commerciaux.val_salaire + self.ventes * Commerciaux.val_salaire

#-----------------------------------------------------------------------------------------------------------------------------------

class Entreprise(Responsable_hierarchique, Commerciaux) :
    def __init__(self):
        pass

    def calcul_salaire_total(self):
        salaire_Employe = Employes.nbr_employe * (Employes.val_salaire * Employes.indice_salaire)
        salaire_responsable = Responsable_hierarchique.nbr_responsable * (Responsable_hierarchique.val_salaire * Responsable_hierarchique.indice_salaire)
        salaire_commerciaux = Commerciaux.val_salaire * Commerciaux.nbr_Commerciaux + Commerciaux.ventes * Commerciaux.val_salaire
        return salaire_commerciaux + salaire_Employe + salaire_responsable
    




user = Employes("chris")
user2 = Commerciaux("Jonh")
user3 = Responsable_hierarchique("Jean")
sale_to_all = Entreprise()
print("\n{}\n".format(user.affichage_caractéristique()))

sal_total = sale_to_all.calcul_salaire_total()
print("le salaire total vaut : ",sal_total)
        


