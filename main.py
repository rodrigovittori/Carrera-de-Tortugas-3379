# [M3.L4] Carrera de tortugas - Actividad # 3 "Campo de carrera"

# NOTA: Ésta es la primera actividad del proyecto

import turtle

t = turtle.Turtle() # Tortuga que dibuja el tablero (t)
t.penup()
t.goto(-100, 100)
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