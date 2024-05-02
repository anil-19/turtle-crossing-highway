from turtle import Turtle
import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE



    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 4:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1.0, stretch_len=2.0)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_Y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_Y)
            self.all_cars.append(new_car)

    def move_forward(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def speed(self):
        self.car_speed +=MOVE_INCREMENT






