import os
import random

def guardar_puntuacion(jugador, puntos):
    puntuaciones = cargar_puntuaciones()
    if jugador in puntuaciones:
        puntuaciones[jugador] += puntos
    else:
        puntuaciones[jugador] = puntos
    with open("puntuaciones.txt", "w") as file:
        for nombre, score in puntuaciones.items():
            file.write(f"{nombre},{score}\n")

def cargar_puntuaciones():
    puntuaciones = {}
    if os.path.exists("puntuaciones.txt"):
        with open("puntuaciones.txt", "r") as file:
            for line in file:
                nombre, score = line.strip().split(",")
                puntuaciones[nombre] = int(score)
    return puntuaciones

def mostrar_puntuaciones():
    puntuaciones = cargar_puntuaciones()
    print("===== PUNTUACIONES =====")
    for jugador, puntos in puntuaciones.items():
        print(f"{jugador}: {puntos} puntos")
    print("=======================")
    input("Presiona ENTER para regresar al menú...")

def jugar(jugador):
    palabras = ["python", "redes", "variables", "programacion", "computadora"]
    palabra_aleatoria = random.choice(palabras)
    palabra_oculta = list("_" * len(palabra_aleatoria))
    intentos = 6
    letras_usadas = []
    
    while intentos > 0 and "_" in palabra_oculta:
        os.system('cls')
        print("Palabra: " + " ".join(palabra_oculta))
        print(f"Intentos restantes: {intentos}")
        print("Letras usadas: " + ", ".join(letras_usadas))
        letra = input("Escribe una letra: ").lower()
        
        if letra in letras_usadas:
            print("Ya usaste esa letra")
            input("Presiona ENTER para seguir...")
            continue
        
        letras_usadas.append(letra)
        if letra in palabra_aleatoria:
            for i, char in enumerate(palabra_aleatoria):
                if char == letra:
                    palabra_oculta[i] = letra
        else:
            intentos -= 1

    os.system('cls')
    if "_" not in palabra_oculta:
        print(f"¡Felicidades, {jugador}, ganaste!")
        guardar_puntuacion(jugador, 10)
    else:
        print(f"¡Perdiste! La palabra era: {palabra_aleatoria}")

def jugar_multijugador(jugador_1, jugador_2):
    jugadores = [jugador_1, jugador_2]
    for ronda in range(2):
        jugador_actual = jugadores[ronda]
        adivinador = jugadores[1 - ronda]
        os.system('cls')
        print(f"{jugador_actual}, elige una palabra para que {adivinador} la adivine:")
        palabra_secreta = input("Ingresa la palabra secreta: ").lower()
        os.system('cls')
        print(f"{adivinador}, es tu turno para adivinar la palabra!")
        
        palabra_oculta = list("_" * len(palabra_secreta))
        intentos = 6
        letras_usadas = []
        
        while intentos > 0 and "_" in palabra_oculta:
            print("Palabra: " + " ".join(palabra_oculta))
            print(f"Intentos restantes: {intentos}")
            print("Letras usadas: " + ", ".join(letras_usadas))
            letra = input("Escribe una letra: ").lower()
            
            if letra in letras_usadas:
                print("Letra repetida. Intenta otra vez.")
                continue
            letras_usadas.append(letra)
            
            if letra in palabra_secreta:
                for i, char in enumerate(palabra_secreta):
                    if char == letra:
                        palabra_oculta[i] = letra
            else:
                intentos -= 1

        if "_" not in palabra_oculta:
            print(f"¡Felicidades {adivinador}! Has adivinado la palabra: {palabra_secreta}")
            guardar_puntuacion(adivinador, 10)
        else:
            print(f"¡Lo siento {adivinador}, has perdido! La palabra era: {palabra_secreta}")

def main():
    while True:
        os.system('cls')
        print("=====================================")
        print("    Bienvenido al juego 'El Ahorcado'")
        print("=====================================")
        print("1. Jugar Vs Computadora")
        print("2. Jugar multijugador")
        print("3. Ver puntuaciones")
        print("4. Salir")
        print("=====================================")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            jugador = input("Ingresa tu nombre: ")
            jugar(jugador)
        elif opcion == "2":
            jugador_1 = input("Nombre del Jugador 1: ")
            jugador_2 = input("Nombre del Jugador 2: ")
            jugar_multijugador(jugador_1, jugador_2)
        elif opcion == "3":
            mostrar_puntuaciones()
        elif opcion == "4":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción inválida.")
            input("Presiona ENTER para continuar...")

if __name__ == "__main__":
    main()
