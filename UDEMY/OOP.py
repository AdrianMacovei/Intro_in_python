# from turtle import Turtle, Screen
#
# timmy = Turtle()
# adi = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.right(100)
# timmy.forward(100)
# timmy.home()
# adi.shape("turtle")
# adi.forward(100)
#
#
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen)
# from turtle import left

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
