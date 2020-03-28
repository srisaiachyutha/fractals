from p5 import *
x,y = width/2,height/2
import random
import math

l=[]
#radius of the circle
radius=350

golden_ratio = 0.61803

n=int(input('enter the no of vertices'))

center_x,center_y= width/2+200,height/2+200

angle = 2*math.pi/n

#to store the points of the vertices generated
for  i in range(1,n+1):
    l.append([center_x+math.sin(angle*i)*radius,center_y+math.cos(angle*i)*radius])
print(l)


def setup():
    #this is the function for the window size setting and also the back_ground color
	size(800,800)
	no_stroke()
	background(0)
	
def draw():
    global x
    global y
    global l
    global golden_ratio
    fill(255,0,0)

    for i in l:
        circle(tuple(i),10) 

    #here we generate a random selection of the points of the generated vertices
    newx,newy=tuple(random.choice(l))

    x,y=(1-golden_ratio )*x+(newx)*golden_ratio ,(1-golden_ratio )*y+(newy)*golden_ratio
    #we move to that point and we make a circle of size 3 and we will repeat this procedure 

    fill(255,0,0)
    circle((x,y),3)


run()
