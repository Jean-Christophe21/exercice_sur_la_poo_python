#définition de la classe des nombres complexes
import copy
from math import sqrt
class Complexe :

    def __init__(self,reel , imaginaire) -> None:
        self.reel = reel 
        self.imaginaire = imaginaire

# cette methode permet la somme de deux nombre complexes
    def sommeNombreComplexe(self, nombre):
        copie = copy.deepcopy(self) 
        if isinstance(nombre, Complexe) :
            copie.reel += nombre.reel
            copie.imaginaire += nombre.imaginaire
            return copie
        else :
            copie.reel += nombre
            return copie


# cette methode permet le produit de deux nombre complexes
    def ProduitNombreComplexe(self, nombre) :
        copie = copy.deepcopy(self) 
        resultat = copy.deepcopy(self) 

        if isinstance(nombre, Complexe) :
            resultat.reel = copie.reel * nombre.reel - copie.imaginaire * nombre.imaginaire
            resultat.imaginaire = copie.reel * nombre.imaginaire + nombre.reel * copie.imaginaire
            return resultat
        else :
            resultat.reel *= nombre
            return resultat
        
    def conjuge(self) : #  permet de calculer le conjugué du nombre complexe sur lequel il est appelé
        copie = copy.deepcopy(self)
        copie.imaginaire = -copie.imaginaire
        return copie
    
    def module(self)-> float :  #  permet de calculer le module du nombre complexe sur lequel il est appelé
        return sqrt(self.reel**2 + self.imaginaire**2) 
    
    
    def carre(self) :  # permet de calculer le produit de deux nombre complexe
        copie = copy.deepcopy(self)
        resultat = copy.deepcopy(self)
        resultat.reel = copie.reel**2 - copie.imaginaire**2
        resultat.imaginaire = 2*(copie.reel * copie.imaginaire)
        return resultat
    
    def afficher_classe(self)->None : # permeT L'affichage d'un nombre complexe
        if self.imaginaire > 0 :
            print(f"{self.reel}+{self.imaginaire}i")
        elif self.imaginaire < 0 :
            print(f"{self.reel} {self.imaginaire}i")
        else :
            print(f"{self.reel}")
        
     
#initialisation des valeurs 
nombre1 = Complexe(1, -2)
nombre2 = Complexe(-3, 1)
nombre3 = Complexe(0, 0)

#affichage des valeurs
print("calcul de la somme de  :")
nombre1.afficher_classe()
print("et")
nombre2.afficher_classe()

#traitement 
nombre3 = nombre1.sommeNombreComplexe(nombre2)

#affichage des valeurs
print("\nle résultat vaut :")
nombre3.afficher_classe()

"""calcul du produit de deux nombres complexes"""
#affichage des valeurs
print("calcul du produit de :")
nombre1.afficher_classe()
print("et de")
nombre2.afficher_classe()

#traitement 
nombre3 = nombre1.ProduitNombreComplexe(nombre2)

#affichage des valeurs
print("\nle produit vaut vaut :")
nombre3.afficher_classe()

"""calcul de l'expression conjugée d'un nombre complexe"""
print("calculons l'expression conjugue de :")
nombre1.afficher_classe()

nombre1.conjuge()

print("après le calcul :")
nombre1.afficher_classe()

"""calcul du carré d'un nombre complexe"""
print("avant le calcul :")
nombre1.afficher_classe()

nombre2 = nombre1.carre()

print("le carré de ce nombre complexe vaut :")
nombre2.afficher_classe()

"""calcul du module d'un nombre complexe"""
print("calcul du module de :")
nombre1.afficher_classe()

module = nombre1.module()

print("le module vaut :", module)

