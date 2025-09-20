# Practica-Graficacion
Repositorio De Trabajos Para La Materia de Graficación

Cómo usar
Ejecutar el programa

Hacer clic en la ventana de Turtle

Usar las flechas del teclado para mover el círculo

Cada flecha mueve el círculo 10 píxeles en esa dirección

Tecnologías utilizadas

Python 3.10

Módulo Turtle para gráficos

circulo = turtle.Turtle()
circulo.shape("circle")
circulo.speed(0)
circulo.penup()

EN ESTAS LINEAS DE CODIGO LLAMO A LA TORTUGA PERO LE DOY FORMA DE CIRCULO EN VEZ DE TORTUGA PARA DARLE LA VELOCIDAD DE LA TORTUGA Y NO TENER QUE HACER LA FIGURA DESDE CERO

def mover_arriba():
    y = circulo.ycor()
    circulo.penup()
    circulo.goto(circulo.xcor(), y + 10)
    circulo.pendown()

def mover_abajo():
    y = circulo.ycor()
    circulo.penup()
    circulo.goto(circulo.xcor(), y - 10)
    circulo.pendown()

def mover_izquierda():
    x = circulo.xcor()
    circulo.penup()
    circulo.goto(x - 10, circulo.ycor())
    circulo.pendown()

def mover_derecha():
    x = circulo.xcor()
    circulo.penup()
    circulo.goto(x + 10, circulo.ycor())
    circulo.pendown()

    EN ESTAS LINEAS DE CODIGO LO QUE HAGO ES DEFINIR LOS MOVIMIENTOS DEL CIRCULO HACIENDO QUE VAYA HACIA ARRIBA, HACIA ABAJO, IZQUIERDA Y DERECHA HACIENDO QUE SE MUEVA A 10 PIXELES PARA DAR LOS SALTOS

    turtle.listen()
turtle.onkey(mover_arriba, "Up")
turtle.onkey(mover_abajo, "Down")
turtle.onkey(mover_izquierda, "Left")
turtle.onkey(mover_derecha, "Right")

turtle.done()

AQUI HAGO QUE LA TORTUGA RESPONDA CON LAS TECLAS PARA QUE SE MUEVA CONFORME PRESIONO LOS BOTONES DEL TECLADO PARA QUE EL CIRCULO SE MUEVA CONFORME PRESIONO LOS BOTONES