import turtle
import time
import random

delay=0.1
score=0
high_score=0

a=turtle.Screen()
a.bgcolor("white")
a.title("SnakeGame")
a.setup(width=600,height=600)
a.tracer(0)

h=turtle.Turtle()
h.speed(0)
h.shape("circle")
h.color("red")
h.penup()
h.goto(0,0)
h.direction="right"

f=turtle.Turtle()
f.speed(0)
f.shape("square")
f.color("green")
f.penup()
f.goto(0,100)

seg=[]

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High-Score: 0",align="center",font=("Courier", 24, "normal"))

def go_up():
    h.direction="up"
def go_down():
    h.direction="down"
def go_right():
    h.direction="right"
def go_left():
    h.direction="left"

def move():
    if h.direction=="up":
        y=h.ycor()
        h.sety(y+20)

    if h.direction=="down":
        y=h.ycor()
        h.sety(y-20)

    if h.direction=="right":
        x=h.xcor()
        h.setx(x+20)

    if h.direction=="left":
        x=h.xcor()
        h.setx(x-20)

a.listen()
a.onkeypress(go_up,"w")
a.onkeypress(go_down,"s")
a.onkeypress(go_right,"d")
a.onkeypress(go_left,"a")

while True:
    a.update()

    if h.xcor()>290 or h.xcor()<-290 or h.ycor()>290 or h.ycor()<-290:
        time.sleep(1)
        h.goto(0,0)
        h.direction="stop"
        for s in seg:
            s.goto(1000,1000)
        seg.clear()

        score=0
        pen.clear()
        pen.write("Score: {}  High-Score: {}".format(score, high_score),align="center",font=("Courier",24,"normal"))

    if h.distance(f)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        f.goto(x,y)

        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("circle")
        new_seg.color("orange")
        new_seg.penup()
        seg.append(new_seg)

        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {}  High-Score: {}".format(score, high_score),align="center",font=("Courier",24,"normal"))

    for i in range(len(seg)-1,0,-1):
        x=seg[i-1].xcor()
        y=seg[i-1].ycor()
        seg[i].goto(x,y)

    if len(seg)>0:
        x=h.xcor()
        y=h.ycor()
        seg[0].goto(x,y)

    move()
    
    for s in seg:
        if s.distance(h)<20:
            time.sleep(1)
            h.goto(0,0)
            h.direction="stop"
            for s in seg:
                s.goto(1000,1000)
            seg.clear()

    time.sleep(delay)

a.mainloop()