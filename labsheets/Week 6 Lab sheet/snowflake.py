import turtle
myscreen = turtle.Screen()

def kochCurve(x,m):
    
    if x<m:
        turtle.forward(x)
    else:
        kochCurve(x/3,m)
        turtle.left(60)
        kochCurve(x/3,m)
        turtle.right(120)
        kochCurve(x/3,m)
        turtle.left(60)
        kochCurve(x/3,m)

#kochCurve(500,50)

def kochSnowflake(x,m):
    turtle.delay(0)
    kochCurve(500,50)
    turtle.left(-120)
    kochCurve(500,50)
    turtle.left(-120)
    kochCurve(500,50)
    turtle.left(-130)


kochSnowflake(500,10)    
myscreen.mainloop()

