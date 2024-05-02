import time
from turtle import Screen
import player
from car_manager import CarManager
import scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = player.Player()
car_manager = CarManager()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(player.Up,'Up')
scoreboard.update()

sleep_time = 0.1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_forward()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            screen.exitonclick()
            game_is_on = False

        if player.ycor() >= 265:
            player.restart()
            car_manager.speed()
            scoreboard.l_point()


