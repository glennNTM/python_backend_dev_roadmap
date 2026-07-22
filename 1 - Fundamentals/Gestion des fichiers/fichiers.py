import json

chemin_00 = "C:/Users/Glenn NTOUTOUME/Documents"
chemin_01 = r"C:\Users\Glenn NTOUTOUME\Documents"

print(chemin_00)
print(chemin_01)


# Utiliser r pour lire la chaine de chaine de charactere en brut

# chemin = "C:/Users/Glenn NTOUTOUME/fichier.txt"
# with open(chemin, "a", encoding='utf-8') as f:
#      # contenu = f.read().splitlines() #['Hello la Terre.', "Python c'est cool."]
#     # print(contenu)
#     f.write("\nBye")

chemin = "C:/Users/Glenn NTOUTOUME/fichier.json"
with open(chemin, "w", encoding='utf-8') as f:
    json.dump(list(range(10)), f, indent=4)