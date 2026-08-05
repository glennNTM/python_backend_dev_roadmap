nom = "Glenn"

def bonjour(name: str) -> str:
    print(f"Bonjour {name}!")

def bye(name: str) -> str:
    print(f"Au revoir {name}!")

if __name__ == "__main__":
    bonjour(nom) 
    bye(nom)