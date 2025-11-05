from turtle import *

#we want to pain a house
#step 1:draw a square
shape("turtle")
speed(7)
color("blue")
width(7)
forward(200)

left(90)

forward(200)
left(90)
forward(200)

left(90)

forward(200)
left(90)
#end of square

#drawin a door
forward(70)

color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
penup()
goto(200,200)

pendown()
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof
penup()
goto(150,150)
pendown()

color("brown")

begin_fill()

right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()

goto(50,150)
pendown()



begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

end_fill()


penup()
goto(70,0)
pendown()
color("red")
begin_fill()
right(180)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()



exitonclick()