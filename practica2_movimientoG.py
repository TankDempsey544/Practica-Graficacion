import turtle

#en esta parte se crea la tortuga con forma de circulo que sera la figura que se movera
circulo = turtle.Turtle()
circulo.shape("circle")
circulo.speed(0)
circulo.penup()

#aqui definiremos los movimientos de la tortuga
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

#aqui definire que el circulo se movera con las flechas del teclado
turtle.listen()
turtle.onkey(mover_arriba, "Up")
turtle.onkey(mover_abajo, "Down")
turtle.onkey(mover_izquierda, "Left")
turtle.onkey(mover_derecha, "Right")

turtle.done()