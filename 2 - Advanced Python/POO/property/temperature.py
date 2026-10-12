class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius < -273.15:
            raise ValueError("La temperature doit etre superieure au zero absolue")
        self._celsius = new_celsius


temp_1 = Temperature(100)
temp_2 = Temperature(100)

print(str(temp_1.fahrenheit)  +"°F")
print(str(temp_1.celsius) +"°C")

temp_2.celsius = 0
temp_1.celsius = -500

