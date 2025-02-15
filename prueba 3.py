
p = float(input("ingrese 1 (De Farenheit a Centigrado) o 2 (De Centigrado a Farenheit): "))
if p == 1:
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    centigrado = (fahrenheit - 32) * 5 / 9
    print(f"La temperatura en centigrados es: {centigrado}")

elif p == 2:
    centigrado = float(input("Ingresa la temperatura en centigrados: "))
    fahrenheit = (centigrado * 9 / 5) + 32
    print(f"La temperatura en Fahrenheit es: {fahrenheit}")
