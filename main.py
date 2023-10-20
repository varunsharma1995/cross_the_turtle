import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.go_up, "Up")
game_is_on = True
level=0

scoreboard = Scoreboard()
car_manager = CarManager()
print(car_manager)

# for _ in range(10):
#     uberFleet.append(CarManager())
speed = .2
while game_is_on:
    time.sleep(speed)
    car_manager.create_car()
    car_manager.move_car()
    screen.update()
    if player.ycor() > 280:
        speed *= .9
        scoreboard.update_score()
    player.reset_position()
    for item in car_manager.cars:
        if item.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            print('game over')

screen.exitonclick()
