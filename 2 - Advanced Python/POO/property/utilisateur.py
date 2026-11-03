# Challenge 3 (Hard) : Utilisateur
# Une classe avec un email et un mot_de_passe :

# email : property avec setter qui valide un format minimal 
# (présence d’un @ et d’un point après) et normalise en minuscules sans espaces ;
# mot_de_passe : écriture seule (le getter lève une exception ou n’existe pas), 
# le setter exige 8 caractères minimum et stocke seulement une version transformée, jamais le texte brut. Une méthode verifier_mot_de_passe compare une saisie au stocké.


import hashlib


class Utilisateur():
    def __init__(self, email: str ):
        self.email = email
        self._mot_de_passe = None

    @property
    def email(self):
        return self._email

    @staticmethod
    def email_normaliser(non_normalised_email: str):
        normalised_email = non_normalised_email.lower().strip().replace(" ", "")

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
       try:
            return self._mot_de_passe
       except:
           AttributeError("Mot de passe inacessible.")

    @staticmethod
    def hacher_mdp(unhashed_mdp: str):
        encoded_mdp = unhashed_mdp.encode()
        hashed_mdp = hashlib.sha256(encoded_mdp).hexdigest()

        return hashed_mdp


    @staticmethod
    def check_mdp(mdp: str):
        mdp_min_length = 8
        if mdp.isspace():
            raise ValueError("Mot de passe invalide.")
        if not isinstance(mdp, str):
            raise TypeError("Le type du mot de passe est invalide.")
        if len(mdp) < mdp_min_length: 
            raise ValueError(f"Le mot de passe est trop court. ({mdp_min_length} caracteres minimum)")
        return mdp
            


    @mot_de_passe.setter
    def mot_de_passe(self, new_mdp: str):
        valid_mdp = Utilisateur.check_mdp(new_mdp)
        
        self._mot_de_passe = Utilisateur.hacher_mdp(valid_mdp)

    
    def verifier_mot_de_passe(self, mdp_saisi: str):
        if not isinstance(mdp_saisi, str):
            raise TypeError("Le mot de passe est invalide. Ca doit etre une chaine de caractere.")
        mdp_stocke = self._mot_de_passe

        return Utilisateur.hacher_mdp(mdp_saisi) == mdp_stocke

# Tests
me = Utilisateur("glennntoutoume@gmail.com")
test = Utilisateur("test@gmail.com")
last = Utilisateur("last@gmail.com")


me.mot_de_passe = "abcdefgh"
test.mot_de_passe = "Abcdefgh"


print(me.mot_de_passe)

# print(me.verifier_mot_de_passe( "mauvais123"))
# print(me.verifier_mot_de_passe( "abcdefgh"))
# print(me.verifier_mot_de_passe( "Abcdefgh"))
# print(me.verifier_mot_de_passe( me.mot_de_passe))
# print(last.verifier_mot_de_passe( "5354468"))




