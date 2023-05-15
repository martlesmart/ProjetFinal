import datetime
import jsonpickle
from pathlib import Path

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
        listreparation=Voiture.get_reparation()
        listreparation.append(element)
        Voiture.set_reparation(self, listreparation)

#  la classe garage
class Garage(object):
#  definition du constructeur
    def __init__(self, nom: str, adresse: str, telephone: str, employes: list[Employe], voiture:list[Voiture]):

        #  initialisation des attributs
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.set_employes(employes)
        self.set_voiture(voiture)

    #  definition des methodes d'acces
    def get_nom(self)->str:
        return self.__nom
    def set_nom(self, value:str):
        self.__nom=value

    def get_adresse(self)->str:
        return self.__adresse
    def set_adresse(self, value:str):
        self.__adresse=value

    def get_telephone(self)->str:
        return self.__telephone
    def set_telephone(self, value:str):
        self.__telephone=value

    def get_employes(self)->list[Employe]:
        return self.__employes
    def set_employes(self, value:list[Employe]):
        self.__employes=value

    def get_voiture(self)->list[Voiture]:
        return self.__voiture
    def set_voiture(self, value:list[Voiture]):
        self.__voiture=value

    #  les methodes utilitaires
    def serialisergarage(cls, element:Garage, fichier:str)->None:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(fichier)
        stream=path.open('w')
        #serialiser la valeur vers un string sous le format json
        strjson:str=jsonpickle.encode(element, indent=4,separators=(',',':'))
        #  ecrire le string vers le fichier
        stream.write(strjson)

        #fermer le stream
        stream.flush()
        stream.close()

    def deserialisergarage(cls, fichier:str)->Garage:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(fichier)
        stream=path.open('r')

        strjson=stream.read()
        #deserialiser la chaine en format json vers un objet vers un objet
        reponse:object=jsonpickle.decode(strjson)

        #fermer le stream
        stream.close()
        #retourner le resultat
        return reponse

    def ajoutervoiture(self, element:Voiture)->None:
        listvoiture = Garage.get_voiture()
        listvoiture.append(element)
        Garage.set_voiture(self, listvoiture)

    def getvoiture(self, numvoiture:str)->Voiture:
        return Garage.getvoiture(numvoiture)


    def ajouterreparation(self, numvoiture:str, reparation:Reparation)->None:
        Voiture.set_reparation(numvoiture)

    def getreparation(self, numvoiture:str)->list[Reparation]:
        return Garage.getreparation(self, numvoiture)
