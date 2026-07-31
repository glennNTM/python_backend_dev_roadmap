# Iterative
def factorielle_1(n: int) -> int:
    facto = 1
    if n <= 1:
        return 1
    else:
        for i in range(1, n + 1):
            facto *= i

        return facto

# Recursivite
def factorielle_2(n: int) -> int:
    facto = 1
    if n <= 1:
        return 1
    facto = n * factorielle_2(n - 1)

    return facto

print(factorielle_2(5))
print(factorielle_1(5))

