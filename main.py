""" [M3.L4] Carrera de tortugas - Actividad # 8 "Aficionados"

Objetivo: Dibujar espectadores para nuestro evento
NOTA: El ejercicio 7 es resuelto por el código de la actividad #6

Paso Nº 1: Creamos una nueva tortuga para dibujar los espectadores
Paso Nº 2: La ponemos en posición
Paso Nº 3: Calculamos un número random de espectadores (por defecto entre 2 y 10)
Paso Nº 4: Escribimos un bucle for que use dib_espectadores para simular varias tortugas

"""
import turtle
import random

# VARIABLES GLOBALES
velocidad_corredores = 5 # Controla la velocidad de la animación int: 0~10 (MAS BAJO, MAS RAPIDO) 
cant_tortugas = 0 #contador con la cantidad de corredores
distancia_entre_tortugas = 40
y_inicial_tortugas = 80
x_inicial_tortugas = -230
#posicion_meta_en_x = x_inicial_tortugas + (cant_secciones_pista * ancho_secciones_pista)

# TORTUGA TABLERO

t = turtle.Turtle() # Tortuga que dibuja el tablero (t)
t.penup()
t.goto(-200, 100)
t.pendown()
t.speed(0)

# Pista de carreras
cant_secciones_pista = 15
ancho_secciones_pista = 20
long_secciones_pista = 150

t.color(0, 0, 0)  # Setea el color a negro

for pista in range(1, (1 + cant_secciones_pista)):
    t.write(str(pista))         # Escribe el número de la seccion (1~15)
    t.right(90)                 # Gira 90º (mirando hacia abajo)
    t.fd(long_secciones_pista)  # Dibuja la línea de la sección
    t.bk(long_secciones_pista)  # Retrocede y "vuelve" arriba
    t.seth(0)                   # Acomoda la tortuga para que quede mirando a la dcha
    t.fd(ancho_secciones_pista) # Avanza el ancho hasta la próxima sección

###################################

t.hideturtle()

# CREAR CORREDORES:

# PRIMERA
cant_tortugas += 1
distancia_recorrida_tortuga_1 = 0
primera = turtle.Turtle() # ROJO
primera.color("crimson")
primera.shape("turtle")
primera.speed(0)
primera.penup()
#primera.goto(-230, 80)
primera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
primera.speed(velocidad_corredores)

# SEGUNDA
cant_tortugas += 1
distancia_recorrida_tortuga_2 = 0
segunda = turtle.Turtle() # AZUL
segunda.color("navy")
segunda.shape("turtle")
segunda.speed(0)
segunda.penup()
#segunda.goto(-230, 40)
segunda.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
segunda.speed(velocidad_corredores)

# TERCERA
cant_tortugas += 1
distancia_recorrida_tortuga_3 = 0
tercera = turtle.Turtle() # AMARILLA
tercera.color("gold")
tercera.shape("turtle")
tercera.speed(0)
tercera.penup()
#tercera.goto(-230, 40)
tercera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
tercera.speed(velocidad_corredores)

# PEDIR PREDICCION USUARIO

opcion_jugador = 0 # Vble global pero la declaramos acá por legibilidad del código

while (opcion_jugador <= 0 or opcion_jugador > cant_tortugas):
    opcion_jugador = int(input("Cual tortuga cree que ganara? (1/2/3): "))

#opcion_jugador = input("Cual tortuga cree que ganara?: ")
t.penup()
t.goto(x_inicial_tortugas + 100, 120)
t.write("Apostaste por la tortuga #" + str(opcion_jugador))
#t.write("Apostaste por la tortuga " + opcion_jugador)

##############################

# DIBUJAR ESPECTADORES

dib_espect = turtle.Turtle()
dib_espect.shape("turtle")
dib_espect.color("purple")
dib_espect.penup()
dib_espect.speed(0)
dib_espect.goto(-190, -120)
dib_espect.seth(90)
dib_espect.speed(velocidad_corredores)

for i in range(1, random.randint(2,11)):
    dib_espect.stamp()
    dib_espect.seth(0)
    dib_espect.fd(distancia_entre_tortugas/2 + 5)
    dib_espect.seth(90)

##############################

# INICIAMOS CARRERA


tenemos_ganadora = False # Vble de control que detendrá el bucle de la carrera cuando haya una ganadora
tortuga_ganadora = 0     # Vable que contiene la id de nuestra ganadora
primera.pendown()
segunda.pendown()
tercera.pendown()

while (not tenemos_ganadora):
    
    if (distancia_recorrida_tortuga_1 > ((cant_secciones_pista + 1) * ancho_secciones_pista)):
        # Si la primera tortuga pasó la línea de meta:
        tortuga_ganadora = 1
        tenemos_ganadora = True
        
    elif (distancia_recorrida_tortuga_2 > ((cant_secciones_pista + 1) * ancho_secciones_pista)):
        # Si la segunda tortuga pasó la línea de meta:
        tortuga_ganadora = 2
        tenemos_ganadora = True
    
    elif (distancia_recorrida_tortuga_3 > ((cant_secciones_pista + 1) * ancho_secciones_pista)):
        # Si la segunda tortuga pasó la línea de meta:
        tortuga_ganadora = 3
        tenemos_ganadora = True
    
    else:
        
        # MOVIMIENTO/AVANCE TORTUGAS
        
        paso_tortuga = random.randint(1, velocidad_corredores) # VELOCIDAD DE AVANCE DE LA TORTUGA
        primera.fd(paso_tortuga)
        distancia_recorrida_tortuga_1 += paso_tortuga
        
        paso_tortuga = random.randint(1, velocidad_corredores) # VELOCIDAD DE AVANCE DE LA TORTUGA
        segunda.fd(paso_tortuga)
        distancia_recorrida_tortuga_2 += paso_tortuga
        
        paso_tortuga = random.randint(1, velocidad_corredores) # VELOCIDAD DE AVANCE DE LA TORTUGA
        tercera.fd(paso_tortuga)
        distancia_recorrida_tortuga_3 += paso_tortuga

### FIN DE LA CARRERA ###

# MOSTRAR TORTUGA GANADORA:
t.penup()
t.goto(x_inicial_tortugas + 100, -80)
win_text = "¡La tortuga #" + str(tortuga_ganadora) + " ha ganado!"
t.write(win_text)

# To-do: agregar condición que compare nuestra predicción con el resultado