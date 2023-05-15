import datetime



# la classe personne
class Personne(object):

#  definition du constructeur de la classe
    def __init__(self, nom = "", prenom = ""):

        # initialisation des attributs
        self.set_nom(nom)
        self.set_prenom(prenom)


# la definition des methodes d'acces
    def get_nom(self) -> str:
        return self.__nom
    def set_nom(self, value : str):
        if 6 > len(value) > 20:
            raise ValueError("le nom doit etre entre 6 et 20 lettre")
        else:
            self.__nom = value

    def get_prenom(self) -> str:
        return self.__prenom
    def set_prenom(self, value : str):
        if 6 > len(value) > 20:
            raise ValueError("le prenom doit etre entre 6 et 20 lettre")
        else:
            self.__prenom = value

#  definition de la methode __str__
    def __str__(self) -> str:
        return f"nom : {self.__nom}"\
        f"\nprenom : {self.__prenom}"

#  la classe employé
class Employe(Personne):
#  definition du constructeur
    def __init__(self, code = 0, fonction = ""):

        #  initialisation des attributs
        self.set_code(code)
        self.set_fonction(fonction)

    #  definition des methodes d'acces
    def get_code(self)->int:
        return self.__code
    def set_code(self, value:int):
        self.__code=value

    def get_fonction(self)->str:
        return self.__fonction
    def set_fonction(self, value:str):
        self.__fonction=value

#  definition de la methode __str__
    def __str__(self) -> str:
        return f"code : {self.__code}"\
        f"\nfonction : {self.__fonction}"

#  la classe client
class Client(Personne):
#  definition du constructeur
    def __init__(self, telephone = "", courriel = ""):

        #  initialisation des attributs
        self.set_telephone(telephone)
        self.set_courriel(courriel)

    #  definition des methodes d'acces
    def get_telephone(self)->str:
        return self.__telephone
    def set_telephone(self, value:str):
        self.__telephone=value

    def get_courriel(self)->str:
        return self.__courriel
    def set_courriel(self, value:str):
        self.__courriel=value

#  definition de la methode __str__
    def __str__(self) -> str:
        return f"telephone : {self.__telephone}"\
        f"\ncourriel : {self.__courriel}"

#  la classe reparation
class Reparation(object):
#  definition du constructeur
    def __init__(self, code: int, description: str, montant: float, datereparation: datetime, codeemploye:int):

        #  initialisation des attributs
        self.set_code(code)
        self.set_description(description)
        self.set_montant(montant)
        self.set_datereparation(datereparation)
        self.set_codeemploye(codeemploye)

    #  definition des methodes d'acces
    def get_code(self)->int:
        return self.__code
    def set_code(self, value:int):
        self.__code=value

    def get_description(self)->str:
        return self.__description
    def set_description(self, value:str):
        self.__description=value

    def get_montant(self)->float:
        return self.__montant
    def set_montant(self, value:float):
        self.__montant=value

    def get_datereparation(self)->datetime:
        return self.__datereparation
    def set_datereparation(self, value:datetime):
        self.__datereparation=value

    def get_codeemploye(self)->int:
        return self.__codeemploye
    def set_codeemploye(self, value:int):
        self.__codeemploye=value

#  la classe voiture
class Voiture(object):
#  definition du constructeur
    def __init__(self, numeroplaque: str, marque: str, modele: str, couleur: str, anne:int, proprietaire:Client, reparation: list[Reparation]):

        #  initialisation des attributs
        self.set_numeroplaque(numeroplaque)
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_couleur(couleur)
        self.set_anne(anne)
        self.set_proprietaire(proprietaire)
        self.set_reparation(reparation)

    #  definition des methodes d'acces
    def get_numeroplaque(self)->str:
        return self.__numeroplaque
    def set_numeroplaque(self, value:str):
        self.__numeroplaque=value

    def get_marque(self)->str:
        return self.__marque
    def set_marque(self, value:str):
        self.__marque=value

    def get_modele(self)->str:
        return self.__modele
    def set_modele(self, value:str):
        self.__modele=value

    def get_couleur(self)->str:
        return self.__couleur
    def set_couleur(self, value:str):
        self.__couleur=value

    def get_anne(self)->int:
        return self.__anne
    def set_anne(self, value:int):
        self.__anne=value

    def get_proprietaire(self)->Client:
        return self.__proprietaire
    def set_proprietaire(self, value:Client):
        self.__proprietaire=value

    def get_reparation(self)->list[Reparation]:
        return self.__reparation
    def set_reparation(self, value:list[Reparation]):
        self.__reparation=value

    #  la methode ajouter reparation
    def ajouterreparation(self, element:Reparation)->None:


