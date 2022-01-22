import turtle

w = turtle.Screen()
w.title('Spiral Helix')
w.bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

t = turtle.Pen()
t.speed(0)

for x in range(500):
    color = colors[x % len(colors)]
    t.pencolor(color)
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done