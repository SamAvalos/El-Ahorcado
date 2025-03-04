import os
import random
import time

def mostrar_menu():

    # os.system('cls') limpia la pantalla (consola) en Windows
    os.system('cls')
    print("=====================================")
    print("    Bienvenido al juego 'El Ahorcado'      ")
    print("=====================================")
    print(" 1. Jugar (modo clasico)")
    print(" 2. Jugar multijugador (2 jugadores)")
    print(" 3. Jugar contra la computadora")
    print(" 4. Como se juega el modo clasico?")
    print(" 5. Como se juega multijugador?")
    print(" 6. Como se juega contra la computadora?")
    print(" 7. Mostar puntuaciones")
    print(" 8. Salir")
    print("=====================================")

def mostrar_como_jugar():
    os.system('cls')
    print("=====================================")
    print("    Como se juega 'El Ahorcado'      ")
    print("=====================================")
    print(" 1. Selecciona una letra")
    print(" 2. Si la letra esta en la palabra, se mostrara en la palabra")
    print(" 3. Si la letra no esta en la palabra, se restara un intento al jugador")
    print(" 4. Tienes 6 intentos para adivinar la palabra")
    print(" 5. Si adivinas la palabra, ganas")
    print(" 6. Si no adivinas la palabra, pierdes")
    print("=====================================")
    input("Presiona ENTER para regresar al menú...")
    os.system('cls')

def mostrar_como_jugar_multijugador():
    os.system('cls')
    print("===============================================================")
    print("    Como se juega 'El Ahorcado' en modo multijugador")
    print("===============================================================")
    print(" 1. Jugador 1 escoge su nombre (asi se guardará tu puntuacion)")
    print(" 2. Jugador 2 escoge su nombre (asi se guardará la puntuacion de ese jugador)")
    print(" 3. Jugador 1 escoge una palabra para que Jugador 2 la adivine")
    print(" 4. Jugador 2 intenta adivinar la palabra de Jugador 1 en los 6 intentos que tiene")
    print(" 5. Luego de que jugador 2 adivine la palabra o pierda, se cambian los roles")
    print(" 6. Jugador 2 escoge una palabra para que Jugador 1 la adivine")
    print(" 7. Jugador 1 intenta adivinar la palabra de Jugador 2 en los 6 intentos que tiene")
    print(" 8. Luego de que jugador 1 adivine la palabra o pierda, se da la opcione de jugar de nuevo o salir al menu")
    print("=====================================")
    input("Presiona ENTER para regresar al menú...")
    os.system('cls')
    
def mostrar_como_jugar_computadora():
    os.system('cls')
    print("===============================================================")
    print("    Como se juega 'El Ahorcado' conta la computadora")
    print("===============================================================")
    print(" 1. Jugador 1 escoge su nombre (asi se guardará tu puntuacion)")
    print(" 2. Jugador 1 tiene 6 oportunidades para adinivar las palabra" )
    print(" 3. Si jugador 1 no adivina la letra se le resta un intento")
    print(" 4. Si adivia la palabra gana 10 puntos")
    print(" 5. si no adivina la palabra pierde")
    print(" 6. Luego jugador 1 escoge una palabra para que la computadora la adivine")
    print(" 7. La computadora tiene 6 intentos para adivinar la palabra")
    print(" 8. Si adivina gana, si no pierde")
    print(" 9. Se da la opcion de jugar de nuevo o salir al menu")
    print("===============================================================")
    input("Presiona ENTER para regresar al menú...")
    os.system('cls')

def puntuaciones(jugador=None):
    # Verificar si el archivo de puntuaciones existe, si no lo crea
    if not os.path.exists("puntuaciones.txt"):
        with open("puntuaciones.txt", "w") as file:
            pass  # Solo crear el archivo vacío si no existe

    if jugador:
        # Mostrar las estadísticas de un jugador específico
        puntuaciones = cargar_puntuaciones()
        if jugador in puntuaciones:
            print(f"Puntuaciones de {jugador}: {puntuaciones[jugador]} puntos")
        else:
            print(f"No se encontró puntuación para el jugador {jugador}.")
    else:
        # Mostrar todas las puntuaciones
        puntuaciones = cargar_puntuaciones()
        if puntuaciones:
            print("===== PUNTUACIONES =====")
            for nombre, score in puntuaciones.items():
                print(f"{nombre}: {score} puntos")
            print("=======================")
        else:
            print("No hay puntuaciones registradas.")
    input("Presiona ENTER para regresar al menú...")

def cargar_puntuaciones():
    puntuaciones = {}
    if os.path.exists("puntuaciones.txt"):
        with open("puntuaciones.txt", "r") as file:
            for line in file:
                nombre, score = line.strip().split(",")
                puntuaciones[nombre] = int(score)
    return puntuaciones

def guardar_puntuacion(jugador, puntos):
    puntuaciones = cargar_puntuaciones()
    if jugador in puntuaciones:
        puntuaciones[jugador] += puntos
    else:
        puntuaciones[jugador] = puntos
    with open("puntuaciones.txt", "w") as file:
        for nombre, score in puntuaciones.items():
            file.write(f"{nombre},{score}\n")

    
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

    print("Bienvenido al juego 'El Ahorcado'")
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

    # Funcion para jugar en modo multijugador
def jugar_multijugador(jugador_1, jugador_2):
    for ronda in range(2):
        if ronda == 0:
            jugador_actual, adivinador = jugador_1, jugador_2
        else:
            jugador_actual, adivinador = jugador_2, jugador_1
        
        # Jugador actual elige una palabra para que el adivinador la adivine
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
            while len(letra) != 1 or not letra.isalpha() or letra in letras_usadas:
                letra = input("Entrada inválida o letra repetida. Intenta otra: ").lower()
            
            letras_usadas.append(letra)
            os.system('cls')
            if letra in palabra_secreta:
                for i, char in enumerate(palabra_secreta):
                    if char == letra:
                        palabra_oculta[i] = letra
                print("¡Bien hecho! Has adivinado una letra.")
            else:
                intentos -= 1
                print("Letra incorrecta. Sigue intentando.")
            
            
        if "_" not in palabra_oculta:
            print(f"¡Felicidades {adivinador}! Has adivinado la palabra: {palabra_secreta}")
        else:
            print(f"¡Lo siento {adivinador}, has perdido! La palabra era: {palabra_secreta}")
        input("Presiona ENTER para continuar...")
    
    while True:
        os.system('cls')
        respuesta = input("¿Quieren jugar de nuevo? (s/n): ").lower()
        if respuesta == 's':
            jugar_multijugador(jugador_2, jugador_1)
            break
        elif respuesta == 'n':
            print("Gracias por jugar!")
            break
        else:
            print("Respuesta inválida. Ingresa 's' para sí o 'n' para no.")

def jugar_vs_computadora(jugador):
    #La computadora elige una palabra para el jugador
    palabras = ["python", "redes", "variables", "programacion", "computadora", "teclado", "mouse", "monitor", "memoria", "almacenamiento"]
    palabra_computadora = random.choice(palabras)
    palabra_oculta = list("_" * len(palabra_computadora))
    intentos = 6
    letras_usadas = []

    print(f"\nBienvenido al juego 'Jugador vs Máquina', {jugador}. Primero, intenta adivinar la palabra de la computadora.")
    print(f"La palabra tiene {len(palabra_computadora)} letras.")

    while intentos > 0 and "_" in palabra_oculta:
        os.system('cls')
        print("Palabra: " + " ".join(palabra_oculta))
        print(f"Tienes {intentos} intentos restantes.")
        print("Letras usadas: " + ", ".join(letras_usadas))

        while True:
            letra = input("Escribe una letra: ").lower()
            if len(letra) == 1 and letra.isalpha():
                break
            else:
                print("Por favor, ingresa una sola letra válida.")

        if letra in letras_usadas:
            print("Ya usaste esa letra.")
            input("Presiona ENTER para continuar...")
            continue

        letras_usadas.append(letra)

        if letra in palabra_computadora:
            for i in range(len(palabra_computadora)):
                if palabra_computadora[i] == letra:
                    palabra_oculta[i] = letra
            print("¡Has adivinado una letra!")
        else:
            intentos -= 1
            print("¡Letra incorrecta! Sigue intentando.")
        input("Presiona ENTER para continuar...")

    os.system('cls')
    if "_" not in palabra_oculta:
        print(f"¡Felicidades, {jugador}, has adivinado la palabra de la computadora!")
        guardar_puntuacion(jugador, 10)
    else:
         print(f"¡Perdiste! La palabra de la computadora era: {palabra_computadora}")
    input("Presiona ENTER para salir...")

    #Ahora la computadora intentará adivinar la palabra del jugador
    os.system('cls')
    print(f"{jugador}, ahora elige una palabra para que la computadora intente adivinarla.")
    palabra_jugador = input("Ingresa tu palabra secreta: ").lower()
    os.system('cls')

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palabra_oculta_computadora = list("_" * len(palabra_jugador))
    intentos_computadora = 6
    letras_usadas_computadora = []
    
    print("\nAhora la computadora intentará adivinar tu palabra...")
    time.sleep(2)  # Pequeña pausa 
    os.system('cls')
    for _ in range(len(alfabeto)):
        if intentos_computadora == 0 or "_" not in palabra_oculta_computadora:
            break  # Terminar si la computadora se queda sin intentos o ya adivinó
        
        # Selección aleatoria de letra por la computadora
        letra_computadora = random.choice([l for l in alfabeto if l not in letras_usadas_computadora])
        letras_usadas_computadora.append(letra_computadora)
        
        os.system('cls')
        print(f"\nIntento de la computadora: {letra_computadora}")
        
        if letra_computadora in palabra_jugador:
            for i in range(len(palabra_jugador)):
                if palabra_jugador[i] == letra_computadora:
                    palabra_oculta_computadora[i] = letra_computadora
            print(f"La computadora adivinó una letra: {letra_computadora}")
        else:
            intentos_computadora -= 1
            print(f"Letra incorrecta, intentos restantes: {intentos_computadora}")
        
        # Mostrar las letras usadas por la computadora
        print("Letras usadas por la computadora: " + ", ".join(letras_usadas_computadora))
        print("Palabra oculta de la computadora: " + " ".join(palabra_oculta_computadora))
        time.sleep(2)  # Pausa para que se vea cada intento uno por uno
        os.system('cls')

    print("\n----------------------------")
    if "_" not in palabra_oculta_computadora:
        print("¡La computadora adivinó tu palabra correctamente!")
    else:
        print(f"La computadora no adivinó tu palabra. La palabra era: {palabra_jugador}")
    print("----------------------------")

    while True:
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta == 's':
            jugar_vs_computadora(jugador)
            break
        elif respuesta == 'n':
            print("Gracias por jugar!")
            break
        else:
            print("Respuesta inválida. Ingresa 's' para sí o 'n' para no.")

def main_jugadores():
    print("Bienvenidos al juego del Ahorcado para 2 jugadores")
    jugador_1 = input("Nombre del Jugador 1: ")
    jugador_2 = input("Nombre del Jugador 2: ")
    
    while True:
        jugar_multijugador(jugador_1, jugador_2)
        input("Presiona ENTER para cambiar de turno...")
        jugar_multijugador(jugador_2, jugador_1)
        
        repetir = input("¿Desean jugar otra vez? (s/n): ").lower()
        if repetir != 's':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            os.system('cls')
            jugador_1 = input("Nombre del Jugador 1: ")
            jugador_2 = input("Nombre del Jugador 2: ")
            jugar_multijugador(jugador_1, jugador_2)
        elif opcion == "3":
            jugador = input("Ingresa tu nombre: ")
            jugar_vs_computadora(jugador)
        elif opcion == "4":
            mostrar_como_jugar()
            os.system('cls')
        elif opcion == "5":
            mostrar_como_jugar_multijugador()
            os.system('cls')
        elif opcion == "6":
            mostrar_como_jugar_computadora()
            os.system('cls')
        elif opcion == "7":
            puntuaciones()
            os.system('cls')
        elif opcion == "8":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción inválida.")
            input("Presiona ENTER para continuar...")
            os.system('cls')

if __name__ == "__main__":
    main()



                    
                
            