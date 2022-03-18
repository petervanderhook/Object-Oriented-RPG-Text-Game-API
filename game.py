from src.globalmap import GlobalMap, MapInstance
from src.character import Character
import time

class Game():
    def __init__(self):
        self.start_time = time.time()
        self.start_time -= 960
        #name = input("What is your name?")
        Character('name')

    def get_name_and_difficulty(self):
        pass
    

    def get_time(self):
        time.sleep(5)
        time_elapsed = time.time() - self.start_time
        hours = int(time_elapsed) // 120
        days = hours // 24
        hours = hours % 24
        minutes = (time_elapsed % 120) / 2

        return f"0{int(days)}:0{int(hours)}:{int(minutes)}"



def main():
    newGame = Game()
    move_prefixes = ['check', 'view']
    while True:
        command = input("What would you like to do?").lower()
        #COMMANDS: 
        # Moving: Prefixes(move, go, head) Postfixes(north, south, west, east, up, down, left, right)
        # Doing: Prefixes(check, view) Postfixes(inventory, time, health, status, character)
        if command == 'check time':
            print(newGame.get_time())
        else:
            print("invalid command")




if __name__ == '__main__':
    main()