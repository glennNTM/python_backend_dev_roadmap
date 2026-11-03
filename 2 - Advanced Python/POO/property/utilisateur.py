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
        if not isinstance(new_email, str):
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

    @staticmethod
    def check_mdp(mdp: str):
        mdp_min_length = 8
        if not isinstance(mdp, str):
            raise TypeError("Le type du mot de passe est invalide.")
        if len(mdp) < mdp_min_length: 
            raise ValueError("Le mot de passe est trop court. (8 caracteres minimum)")
        return mdp
        
            


    @mot_de_passe.setter
    def mot_de_passe(self, new_mdp: str):
        valid_mdp = Utilisateur.check_mdp(new_mdp)
        encoded_mdp = valid_mdp.encode()

        s = hashlib.sha256(encoded_mdp).hexdigest()

        self._mot_de_passe = s

# Tests
me = Utilisateur("glennntoutoume@gmail.com")
test = Utilisateur("test@gmail.com")

me.mot_de_passe = "abcdefgh"
test.mot_de_passe = "Abcdefgh"


print(me.mot_de_passe)
print(test.mot_de_passe)