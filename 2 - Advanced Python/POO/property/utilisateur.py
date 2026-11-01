import hashlib


class Utilisateur():
    def __init__(self, email: str):
        self.email = email

    @property
    def email(self):
        return self._email

    @staticmethod
    def email_normaliser(non_normalised_email: str):
        normalised_email = non_normalised_email.lower().strip()

        return normalised_email
                  
    @email.setter
    def email(self, new_email: str) -> None:
        if type(new_email) != str:
            raise TypeError("L'email doit etre une chaine de caratere")
        email = Utilisateur.email_normaliser(new_email)
        if not email:
            raise ValueError("Email invalide.")
        n = email.count("@")
        if n != 1: 
            raise ValueError("Email entre n'est pas au bon format.")
        local = email.split("@")[0]
        domaine = email.split("@")[1]
        if not "." in domaine or not local: 
            raise ValueError("Email entre n'est pas au bon format.")
        if domaine.startswith(".") or domaine.endswith("."):
            raise ValueError("Email entre n'est pas au bon format.")

        self._email = email
             


    @property
    def mot_de_passe(self):
        return self._mot_de_passe