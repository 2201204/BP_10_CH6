7.
import turtle
t=turtle.Turtle()
t.shape('turtle')
t.left(90) #왼쪽으로 90도 회전함
for i in range(6): #밑의 과정을 6번 반복함
    t.right(60)
    t.forward(100); t.forward(-30); t.left(60); t.forward(30); t.forward(-30);  #앞으로 100만큼 이동하고 뒤로 30만큼 이동하고
                                                                                #왼쪽으로 60도 회전하여 앞으로 30만큼 이동하고 30만큼 뒤로 이동한다.
    t.right(120); t.forward(30); t.forward(-30); t.left(60); t.forward(-70)     #오른쪽으로 120도 회전하여 앞으로 30만큼 이동하고, 30만큼 뒤로 이동한다.
                                                                                #왼쪽으로 60도 회전하여 #중앙으로 되돌아온다.
    
    8.
    import turtle
t=turtle.Turtle()
for i in range(10):
    for i in range(5):
        t.left(144); t. forward(100)
    t.left(10)
    
9.
import random
import turtle
t=turtle.Turtle()
t.shape('turtle')
for i in range(10):
    r=random.randint(1.100)
    r1=random.randint(1.100)
    r2=random.randint(1.100)
    t.circle(r)
    t.up()
    t.goto(r1,r2)
    t.down()
    
    10.
    import random
import turtle
t=turtle.Turtle()
t.shape('turtle')
for i in range(5):
    t.forward(100); t.right(90); t.forward(10); t.right(90); t.forward(100);
    t.left(90); t. forward(10); t.left(90)
    
11.
import random
import turtle
t=turtle.Turtle()
t.shape('turtle')
t.color('red','yellow')
t.begin_fill()
while True:
    t.fd(200); t.lt(170);
    if abs(t.pos()) <1: break
t.end_fill()

12.
import turtle
import math
t=turtle.Turtle()
t.shape('turtle')
t.color('red','yellow')
for i in range(360):
    t.goto(i,200*math.sin(3.14*i/180.0))
