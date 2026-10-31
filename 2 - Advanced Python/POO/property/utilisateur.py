import hashlib


class Utilisateur():
    def __init__(self, email: str):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: str) -> None:
        normalised_email = new_email.lower()
        if "@" in  normalised_email:
            suffixe = normalised_email.split("@")[1]
            if "." in suffixe:
                self._email = normalised_email
        raise ValueError("L'email entre n'est pas correct")
    
        
             


    @property
    def mot_de_passe():
            pass