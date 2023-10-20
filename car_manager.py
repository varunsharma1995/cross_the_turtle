from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_choice = randint(1,6)
        if random_choice ==2:
            car = Turtle()
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.shape('square')
            car.penup()
            car.goto(randint(230, 280), randint(-280, 280))
            car.setheading(180)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(10)

    # def uberFleet(self):
    #     for _ in range(10):
    #         car = self.uber()
    #         self.cars.append(car)
    #
    # def uber(self):
    #     car = Turtle()
    #     car.color(choice(COLORS))
    #     car.shapesize(stretch_wid=1, stretch_len=2)
    #     car.shape('square')
    #     car.penup()
    #     car.goto(randint(230, 280), randint(-280, 280))
    #     car.setheading(180)
    #     return car
    #
    # def move(self):
    #     for car in self.cars:
    #         car.forward(MOVE_INCREMENT)
