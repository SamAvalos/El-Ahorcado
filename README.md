# El Ahorcado

## Descripción
"El Ahorcado" es un juego clásico de adivinanza de palabras. En este caso el jugador tiene que adivinar una palabra oculta, seleccionando letras. Si la letra está en la palabra, se revela en su posición correcta. Si la letra no está en la palabra, se le resta un intento al jugador. El jugador tiene un máximo de 6 intentos para adivinar la palabra. Si el jugador llega a perder sus 6 intentos, el perdera la partida y tendra la oportunidad de jugar otra vez o salir al menu.

El jugador tiene la oportunidad de 3 modos de juego.
   - Modo Clasico (1 jugador)
   - Modo Multijugador (2 jugadores)
   - Modo Jugador contra computadora

## Estado del proyecto
Este proyecto está completo y en funcionamiento. No se planifican cambios significativos, aunque se puede ampliar su compatibilidad, ya que solo esta disponible en el sistema operativo **Windows**.

## Guía de usuario

1. Al inicio del juego, se muestra un menú con las siguientes opciones:
   - **Jugar**: Inicia el juego **El Ahorcado**
   - **¿Cómo se juega?**: Muestra como se juega el juego y sus reglas
   - **Salir**: Cierra el juego.

2. Durante el juego:
   - La palabra se presenta oculta con guiones bajos.
   - El jugador tiene 6 intentos para adivinar la palabra.
   - El jugador debe ingresar una letra a la vez.
   - Si la letra está en la palabra, se revela en su posición.
   - Si la letra no está en la palabra, el intento se descuenta

3. El juego termina cuando el jugador adivina la palabra o agota sus intentos.

4. Después de cada juego, el jugador puede escoger por jugar nuevamente o salir.

## Instalacion

1. Puedes clonar este repositorio o el codigo fuente
```
git clone https://github.com/SamAvalos/El-Ahorcado.git
```
2. Accede a la carpeta del proyecto
```
cd El-Ahorcado
```

## Cómo Jugar
1. Ejecuta el archivo del juego
```
python Juego_El_Ahorcado.py
```
## ACTUALIZAR (SI YA LO TIENES INSTALADO CON UNA VERSION ANTIGUA)

1. Accede a la carpeta del proyecto
```
cd El-Ahorcado
```
2.Actualizar los cambios realizados
```
git pull origin main
```

## Cómo Jugar
1. Ejecuta el archivo del juego
```
python Juego_El_Ahorcado.py
```
## Menú Principal

Al iniciar el juego, verás las siguientes opciones:

1. Jugar: Comenzar una nueva partida.

2. Cómo se juega?: Muestra las reglas del juego.

3. Salir: Cierra el juego.

## Reglas del Juego

- Se elige una palabra aleatoria de una lista predefinida.

- El jugador debe adivinar la palabra letra por letra.

- Si la letra está en la palabra, se revelará en su posición.

- Si la letra no está en la palabra, se pierde un intento.

- El jugador tiene un máximo de 6 intentos antes de perder la partida.

- Si el jugador adivina la palabra completa antes de que se acaben los intentos, gana la partida.

## Mejoras Futuras
Algunas posibles mejoras para el juego:

- Implementar un sistema de puntuación.

- Agregar múltiples niveles de dificultad.

- Dibujar el ahorcado visualmente en ASCII.
