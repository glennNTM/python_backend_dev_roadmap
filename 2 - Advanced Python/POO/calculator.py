class Calculator:
    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Returns the difference between two numbers."""
        return a - b


# Calling a static method on the class
print(Calculator.add(5, 7))  # Output: 12

# Calling a static method on an instance
calculator = Calculator()
print(calculator.subtract(5, 7))  # Output: -2