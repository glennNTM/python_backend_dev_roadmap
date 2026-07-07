# Une fonction masquer_email(email) qui prend une adresse email et masque une partie de l'identifiant local (avant le @) par des astérisques, en gardant seulement le premier et le dernier caractère visibles.

def  masquer_email(email:str) -> str:
    email = email.split("@")
    domaine = email[-1]
    header = email[0]
    premier_char = email[0][0]
    last_char = email[0][-1]
    etoiles = '*' * (len(header) - 2)

    
    return f"{premier_char}{etoiles}{last_char}@{domaine}"

print(masquer_email("glennntoutoume8@gmail.com"))