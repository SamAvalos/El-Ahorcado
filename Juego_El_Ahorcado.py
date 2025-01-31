import os
import random

def mostrar_menu():

    # os.system('cls') limpia la pantalla (consola) en Windows
    os.system('cls')
    print("=====================================")
    print("    Bienvenido al juego 'El Ahorcado'      ")
    print("=====================================")
    print(" 1. Jugar")
    print(" 2. Como se juega?")
    print(" 3. Salir")
    print("=====================================")

def mostrar_como_jugar():
    os.system('cls')
    print("=====================================")
    print("    Como se juega 'El Ahorcado'      ")
    print("=====================================")
    print(" 1. Selecciona una letra")
    print(" 2. Si la letra esta en la palabra, se mostrara en la palabra")
    print(" 3. Si la letra no esta en la palabra, se dibujara una parte del ahorcado")
    print(" 4. Tienes 6 intentos para adivinar la palabra")
    print(" 5. Si adivinas la palabra, ganas")
    print(" 6. Si no adivinas la palabra, pierdes")
    print("=====================================")
    input("Presiona ENTER para regresar al menú...")
    
def jugar():

    # La variable palabras es una lista que contiene las palabras que se pueden adivinar
    palabras = [ "phyton", "redes", "variables", "programacion", "computadora", "teclado", "mouse", "monitor", "memoria", "almacenamiento" , "inteligencia", "algoritmos", "ciclos", "condicionales", "funciones", "clases", "objetos", "herencia", "ingenieria", "sistemas", "cyberseguridad", "trabajo", "codificacion"] 

    # Esta variable elige una palabra aleatoria de la lista palabras
    palabra_aleatoria = random.choice(palabras)

    # Se muestra la palabra pero oculta con  los guiones bajos (cada guion representa una letra de la palabra
    palabra_oculta = list("_" * len(palabra_aleatoria))

    # Numero de intentos del jugador
    intentos = 6

    # Lista para almacenar las letras ya usadas por el jugador
    letras_usadas = []

    print("Bienvendio al juego 'El Ahorcado'")
    print("la palabra tiene ", len(palabra_aleatoria), " letras")
    print("Tienes unicamente ", intentos, " intentos para adivinar la palabra")
    print(" ".join(palabra_oculta))

    while intentos > 0 and "_" in palabra_oculta:
        os.system('cls')
        print("Palabra " + " ".join(palabra_oculta))
        print(f"Tienes {intentos} intentos")
        print("Letras usadas: " + ", ".join(letras_usadas))

        while True:
            letra = input("Escribe una letra: ").lower()
            if len(letra) == 1 and letra.isalpha():
                break  # Solo aceptamos una letra válida
            else:
                print("Por favor, ingresa una sola letra.")

        if letra in letras_usadas:
            print("Ya usaste esa letra")
            input("Presiona ENTER para seguir jugando :)")
            continue
        
        letras_usadas.append(letra)

        if letra in palabra_aleatoria:
            for i in range(len(palabra_aleatoria)):
                if palabra_aleatoria[i] == letra:
                    palabra_oculta[i] = letra
                    print("Has adivinado una letra, muy bien! Sigue intentando")
        else:
            intentos -= 1
            print("Letra incorrecta! :( , sigue intentando") 

        input("Presiona ENTER para seguir intentando :)")

    os.system('cls')
    if "_" not in palabra_oculta:
        print("¡Felicidades, has ganado! :D")
    else:
        print(f"¡Perdiste! La palabra era: {palabra_aleatoria}")
     

    while True:
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta == 's':
            jugar()
            break
        elif respuesta == 'n':
            print("Gracias por jugar!")
            break
        else:
            print("Respuesta inválida. Ingresa 's' para sí o 'n' para no.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_como_jugar()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
            input("Presiona ENTER para continuar...")

if __name__ == "__main__":
    main()



                    
                
            