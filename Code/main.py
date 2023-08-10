"""Import random module."""
import random 
import time
import datetime

HELP_COMMANDS = """
COMMANDS:
SLEEP               : /sleep
EAT                 : /eat
DRINK               : /drink
BACKPACK            : /backpack
READ                : /read
TALK                : /talk

chech backpack => /backpack
    to use something on backpack type "/backpack use {item_name}"
    e.g. => /backpack/drink water
"""

# CONSTANTS
CURRENT_DATETIME = datetime.datetime(2022, 3, 1, 8, 0)
CURRENT_LOCATION = "HOME"


class Game:
    """---"""
    def __init__(self):
        self.name = None
        self.health = 100
        self.hunger = 100
        self.thirst = 100
        self.logic = 0
        self.energy = 100  #--
        self.main_menu_options = f"""
{CURRENT_DATETIME}
\tLOCATION:\t{CURRENT_LOCATION}

HEALTH: {self.health}\t HUNGER: {self.hunger}\t THIRST: {self.thirst}
ENERGY: {self.energy}\t LOGIC: {self.logic}

[TYPE COMMAND OR TYPE "/HELP" TO GET HELP!]
"""
        # --

    # module for game start
    def start_game(self):
        """This is a method that will be shown at the beginning of the game"""
        self.name = input("Enter your name :> ")
        print(f"Hello {self.name}! Welcome to Sim City.")
        self.main_menu() # --

    # function: main menu
    def main_menu(self):
        """---"""
        print(self.main_menu_options)
        command = input("CMD ::> ")
        command = command.lower().strip()

        if command == "/help":
            print(HELP_COMMANDS)
        elif command == "/read":
            self.read()
        elif command == "/drink":
            self.drink()
        elif command == "/eat":
            self.eat()
        elif command == "/sleep":
            if self.hunger >= 60 and self.energy <= 50 and self.thirst >= 30:
                self.sleep()
            else:
                if self.energy > 50:
                    print("Player cannot sleep now! energy is too high")
                elif self.hunger < 60:
                    print("I need to eat something")
                else:
                    print("I'm too thirsty.. I need something to drink!")
                self.main_menu()

    # function for eating
    def eat(self, item=None):
        """---"""
        print(f"Player has eaten..{item}")
        self.hunger += 30

    # function for drinking
    def drink(self, item=None):
        """---"""
        print(f"Player has drank..{item}")
        self.thirst += 30
        
    # module for player sleeping
    def sleep(self):
        """if the player sleeps:
            energy = 100, health += 10, thirst -= 30, hunger -= 50
            day += 1, time = 08:00, location = home
        """
        global CURRENT_DATETIME, CURRENT_LOCATION
        # updating all the stats
        self.energy = 100
        self.health = 100
        self.thirst -= 30
        self.hunger -= 70

        # updating time
        sleeping_hours = datetime.timedelta(hours=8)
        CURRENT_DATETIME += sleeping_hours
        CURRENT_LOCATION = "HOME"

        print("Player has slept")
        self.update()           # update game
        self.main_menu()        # return to the main menu

    # function for reading
    def read(self, item=None):
        """---"""
        global CURRENT_DATETIME
        print("Reading..")
        print(item)
        self.energy -= 30
        CURRENT_DATETIME += datetime.timedelta(hours=1)

        # update and return to main menu
        self.update()
        self.main_menu()

    # function: updating game
    def update(self):
        """---"""
        self.main_menu_options = f"""
{CURRENT_DATETIME}
\tLOCATION:\t{CURRENT_LOCATION}

HEALTH: {self.health}\t HUNGER: {self.hunger}\t THIRST: {self.thirst}
ENERGY: {self.energy}\t LOGIC: {self.logic}

[TYPE COMMAND OR TYPE "/HELP" TO GET HELP!]
"""

if __name__ == "__main__":
    City_Sim = Game()
    City_Sim.start_game()
    