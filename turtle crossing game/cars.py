from turtle import Turtle
import random

number_of_cars = 30
cars_list = []
for i in range(number_of_cars):
    cars_list.append(i)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        cars = []
        for n in cars_list:
            car = Turtle("square")
            random.shuffle(colors)
            car.color(colors[0])
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.pu()
            car.speed("fastest")
            car.setheading(180)
            x = random.randint(320, 920)
            y = random.randint(-280, 280)
            car.goto(x, y)
            car.speed("normal")
            cars.append(car)
        self.cars = cars
        self.x_speed = 10

    def move(self):
        for car in self.cars:
            x = car.xcor() - self.x_speed
            car.goto(x, car.ycor())

    def refresh(self, car):
        y = random.randint(-280, 280)
        x = random.randint(320, 620)
        random.shuffle(colors)
        car.color(colors[0])
        car.goto(x, y)
