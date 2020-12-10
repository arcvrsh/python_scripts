"""import turtle
sp = turtle.Turtle()
wn = turtle.Screen()
wn.title('Spiro')
wn.bgcolor("black")
sp.speed(0)
for i in range(20):
    for colors in ['violet','indigo','blue','green','yellow','orange','red']:
        sp.color(colors)
        sp.fd(50)
        sp.rt(144)

        
          
sp.ht()
wn.exitonclick()"""

#square in & out
"""import turtle  #Inside_Out 
wn = turtle.Screen() 
wn.bgcolor("light green") 
skk = turtle.Turtle() 
skk.color("blue") 
skk.speed(0)  
def sqrfunc(size): 
    for i in range(20):
        skk.fd(-100) 
        skk.fd(size) 
        skk.left(150) 
        size = size + 10
        skk.fd(400)
sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46) 
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146)
sqrfunc(166)
skk.ht() 
wn.exitonclick()"""

"""import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) """

#turtle stamp
import turtle
win = turtle.Screen()
win.bgcolor('green')
tort = turtle.Turtle()
tort.color('blue')
tort.shape('turtle')
tort.up()
for size in range(5, 200, 2): 
    tort.stamp()  
    tort.forward(size)
    tort.right(50)