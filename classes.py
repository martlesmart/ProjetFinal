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
