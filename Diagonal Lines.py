#SETUP
import turtle as t
t.shape('turtle')
t.speed(999)
t.bgcolor('black')   #for color of thin black lines.

thicc=50                    #Controls the thiccness of the lines.
#thicc = int(t.numinput('Line thingy.py', 'How juicy thicc do you want your lines?'))   #Left commented because it may be an inconvenience but is still cool .

t.penup()
t.pensize(thicc)
t.goto(-870+thicc, 760+thicc)
t.pendown()
#t.goto(0, 0)
y = 1   #y keeps edge in uniform.
f = thicc*2/1.5   #f   =   forward

col=['yellow', 'green']
ncolv=1                   #ncolv   =   next color variant

#LINES
while True:
    ncolv = ncolv +1
    t.pencolor(col[ncolv%2])   #<---   Edit number here to match col list variable if extra colors are added
    t.left(45)     #long side
    t.forward(y)
    t.right(135)   #short side (edge)
    t.forward(f*1.2)    #                  To get rid of thin lines make sure that (f) without anything extra in parenthesis is present.
    y = y + thicc*2
    
    ncolv = ncolv +1
    t.pencolor(col[ncolv%2])   #<---   Edit
    t.right(45)     #long side
    t.forward(y)
    t.left(135)   #short side (edge)
    t.forward(f*1.2)   #                   Here too.
    y = y + thicc*2
    
