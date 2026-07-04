# Manipulation des entiers(int) et decimaux(float)
# Fonction qui convertit une température de Celsius en Fahrenheit, avec le résultat arrondi à 2 décimales. 

def celsius_to_fahreinheit(temp: int | float) -> float:
    temp = (temp * 1.8) + 32
    return round(temp, 2)


celsius_to_fahreinheit(30.5)