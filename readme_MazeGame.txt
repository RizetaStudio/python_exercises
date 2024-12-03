
======================================
               Maze Game
======================================

Este proyecto es un juego de snake desarrollado en Python. 
El juego presenta un entorno dinámico con obstáculos, recolección de objetos y un sistema de movimiento basado en teclas. 
Demuestra conceptos avanzados como bucles, listas, manejo de posiciones, y lógica de colisión.


Descripción del juego:
----------------------
- **Objetivo:** Moverse por el laberinto, recolectar objetos (*) y evitar colisiones con la cola del personaje o los obstáculos.

- **Inicio:** El jugador comienza en una posición inicial y puede moverse utilizando las teclas WASD.

- **Cola dinámica:** Cada objeto recolectado aumenta la longitud de la cola del personaje.

- **Fin del juego:** El juego termina si el jugador choca con su propia cola o decide salir presionando la tecla "P".


Características del código:
---------------------------
1. **Generación de mapa:** 
   - Obstáculos definidos previamente en un diseño textual.
   - Generación aleatoria de objetos en el mapa.

2. **Movimiento del personaje:**
   - Utiliza las teclas WASD para desplazarse.
   - Movimiento continuo en un bucle principal, con verificación de colisiones.

3. **Interactividad:**
   - Recolección de objetos que incrementa la longitud de la cola.
   - Visualización del progreso en tiempo real con una interfaz de texto.

4. **Gestión de colisiones:**
   - Detección de colisiones con obstáculos y cola propia.

Requisitos:
-----------
- Python 3.x
- Librería `readchar` para capturar entradas de teclado en tiempo real.

Cómo ejecutar el juego:
-----------------------
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala la librería `readchar` ejecutando el siguiente comando:
   ```bash
   pip install readchar
   ```
3. Ejecuta el archivo del juego:
   ```bash
   python Maze_game.py
   ```
4. Usa las teclas WASD para moverte y la tecla "P" para salir.


Objetivo del proyecto:
----------------------
Este ejercicio busca reforzar habilidades como:
- Manejo de listas y matrices bidimensionales.
- Implementación de lógica interactiva en bucles.
- Uso de entradas dinámicas para crear experiencias inmersivas.


Contacto:
---------
Si tienes sugerencias, preguntas o simplemente quieres conectar, no dudes en escribirme. ¡Estoy abierto a colaborar y mejorar!
mi mail: enrik.cv@gmail.com
