""" [M3.L4] Carrera de tortugas - Actividad # 4 "Dos Jugadores"

Objetivo: Crear las primeras DOS participantes de nuestra carrera de tortugas

Paso 1: Agregamos variables globales
Paso 2: Creamos nuestras tortugas y las colocamos en el punto de partida

"""
import turtle

# VARIABLES GLOBALES
velocidad_corredores = 5 # Controla la velocidad de la animación int: 0~10 (MAS BAJO, MAS RAPIDO) 
cant_tortugas = 0 #contador con la cantidad de corredores
distancia_entre_tortugas = 40
y_inicial_tortugas = 80
x_inicial_tortugas = -230

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

# CREAR CORREDORES:

# PRIMERA
cant_tortugas += 1
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
segunda = turtle.Turtle() # AZUL
segunda.color("navy")
segunda.shape("turtle")
segunda.speed(0)
segunda.penup()
#segunda.goto(-230, 40)
segunda.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
segunda.speed(velocidad_corredores)