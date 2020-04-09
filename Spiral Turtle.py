                  #  Successful

import turtle
from random import randint as r


turtle.bgcolor("black")
pen = turtle.Turtle()

# r = random.randint   <-<-<-<-   U can also use this type of declearation for this u have to import random lib only. like : import random

width = 20     #  does not matter u can also comment width & height
height = 8
distance = 20          #  distance between two dots

#pen.penup()             #  it will not create normal line; for calling dot() func here we get dots.
list_colour = ["white","yellow","brown","red","orchid4","blue","royalblue1","green","seagreen4","orange","dodgerblue4","pink","violet","grey","cyan"]
pen.setpos(-200,200)               #  (x,y)   cordinate location 

def spiral(m,n) :
    k = l = 0                           #  k = index  of  starting  row
    flag = 0                             #  l = index  of  starting  column

    
                                        # m = number  of  rows 
    while(k<m and l<n) :        # n = number  of  column

        col = r(0,10)                                   #''' if u use this 2 line before while loop then then
        pen.color(list_colour[col])                #1st row colour== 1st column colour '''
        if(flag==1) :
            pen.right(90)
#  printing  the  first  row from the remaining rows      
        for i in range(l,  n) :
            pen.dot()                 #  its a func() for creating  dots.
            pen.forward(distance)
            '''print([k][i], end = " ")'''              
        k+=1
        flag=1
        
# printing the last column from the remaining column        
        pen.right(90)
        col = r(0,10)
        pen.color(list_colour[col])
        for i in range(k,m) :
            pen.dot()
            pen.forward(distance)
            '''print([i][n-1], end = " ")'''
        n-=1
        
# printing the last row from remaining rows
        pen.right(90)
        col = r(0,10)
        pen.color(list_colour[col])
        if(k<m) :

            for i in range(n-1,l-1,-1) :
                pen.dot()
                pen.forward(distance)
                '''print([m-1][i], end = " ")'''
            m-=1
            
# printing the first column from the remaining columns
        pen.right(90)
        col = r(0,10)
        pen.color(list_colour[col])
        if(l<n) :

            for i in range(m-1,k-1,-1) :
                pen.dot()
                pen.forward(distance)
                '''print([i][l], end = " ")'''
            l+=1

'''a = []
count = 1
for i in range(5) :
    p = []
    for j in range(5) :
        p.append(count)
        count+=1
    a.append(p)'''

spiral(20,20)
turtle.done()

