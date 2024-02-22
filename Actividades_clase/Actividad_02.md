# Actividad 02: Graficación y modelamiento básico



1. Escribir un programa en python en el que ingresada
la profundidad máxima, cálcule punto a punto la variación de presión con la profundidad. Para ello el usuario deberá definir un valor  máximo  `y`  en metros y el programa deberá retornar la grafica de Presión como función de `y`. La gráfica deberá tener:

 - Unidades, titulo, fontsize=xticks=14
 - El label de la gráfica deberá indicar el numero de presiones atmosfericas a la que se esta sometida en produndidad máxima. 

Se deberá entregar un archivo con extensión .ipynb llamado activdad_02 y una gráfica para una profundidad de 30m llamada activdad_02_graf.png.


2. Un jugador de baloncesto decide lanzar su balón a una distancia d del aro, con una   rapidez v y ángulo theta respecto a la horizontal. Si  la cesta tiene una altura de 3m, y el movimiento que realiza la pelota es un movimiento parabólico, construya un programa que determine si el jugador de baloncesto 
encesto o no encesto. Para ello: 

- Definido theta, vo, y d como archivo json,  se determine si el jugador encesto o no encesto.

- Construir la gráfica del movimiento parabólico, para un theta, vo, y d, de tal forma que el jugador  enceste.


```python 
import json
 
# Opening JSON file
f = open('data.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()
```
