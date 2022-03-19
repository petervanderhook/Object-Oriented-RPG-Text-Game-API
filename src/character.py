# Authors: Peter Vanderhook and Victor Polemeni
# Date: March 11th, 2022
from src.item import Gear


class Character():
    
    def __init__(self, name):
        """Creates a character.
        Stats are stored in a dictionary.
        xp to next level increases on levelup, xp is not reset
        
        list for status effects, not sure how I will implement this yet. Maybe via 'time' module."""
        self.name = name
        self.skillpoints = 4
        self.level = 1
        self.coins = 0
        self.skills = { "attack": 4, 'strength': 4, "defense": 3, "wisdom": 3, "agility": 3, "luck": 3, "health": 10}
        self.exp = 0
        self.exp_to_level = 69
        self.status = {'poison': False, 'bleed': False, 'fear': False}
        sack = Gear("Old Leather Pouch", capacity=4, value=2, weight=1, slot='back')
        dagger = Gear("Rusty Dagger", weight=1, stats={'attack': 1, 'strength': 1, 'defense': 0, 'wisdom': 0, 'agility': 0, 'luck': 0, 'health': 0}, slot='weapon')
        self.equipment = {'pouch': sack, 'helmet': None, 'armor': None, 'amulet': None, 'ring': None, 'gloves': None, 'back': None, 'boots': None, 'weapon': dagger, 'offhand': None}
        self.capacity = sack.capacity
        self.inventory = []
       
        

    def unequip(self, item: Gear):
        if str(item.slot).lower() == 'pouch':
            print("Unable to manipulate this slot.")
            return 0

    def equip(self, item: Gear):    
        try:
            print("checking this " +str(item.slot))
            if self.equipment[str(item.slot)] != None:
                print("Equipment slot is already occupied!")
                return 0
            self.equipment[str(item.slot)] = item
            self.capacity += item.capacity


            print("Equipped " + str(item.name))

        except KeyError:
            print("Unable to equip this item.")
            return 0
        

    def level_up(self):
        """Levels up. Run this function after xp gain if xp > exp to level.

        Grants 2 skill points and runs loop forcing the user to assign all points
        """
        self.exp_to_level = round(self.exp_to_level * 1.44)
        self.skillpoints += 2
        while self.skillpoints > 0:
            try:
                print(f"Skills:\nAttack - {self.skills['attack']}\nDefense - {self.skills['defense']}\nWisdom - {self.skills['wisdom']}\nAgility - {self.skills['agility']}\nHealth - {self.skills['health']} (+2 per skill point)\nLuck - {self.skills['luck']}")
                choice = input(f"What would you like to improve? You have {self.skillpoints} skill points.\nChoices: 'attack' 'defense' 'wisdom' 'agility' 'health' 'luck'").lower()
                if choice == "health":
                    self.skills['health'] += 2
                    self.skillpoints -= 1
                else:
                    self.skills[choice] += 1
                    self.skillpoints -= 1
                    continue
            except (AttributeError, KeyError):
                print("Please enter a valid choice")
                print('\n' * 100)
    
    def show_equipment(self):
        for item in self.equipment:
            if str(item) == 'pouch':
                continue
            if self.equipment[str(item)] != None:
                print('\n' + str(self.equipment[str(item)]) + " equipped in the "+ str(item) + " slot.")
                for stat in self.equipment[str(item)].stats:
                    if self.equipment[str(item)].stats[str(stat)] > 0:
                        print(f"Grants +{self.equipment[str(item)].stats[str(stat)]} to {stat}.")
            else:
                print('\n' + "Nothing equipped in the " + str(item) + " slot.")
    
    def __repr__(self):
        #make this look good later
        status_effects = ""
        if self.status['poison']:
            status_effects += 'Poisoned'
        if self.status['bleed']:
            status_effects += 'Bleeding'
        if self.status['fear']:
            status_effects += 'Feared'
        if status_effects == "":
            status_effects += 'None'
        return f"========== {self.name} ==========\nLevel: {self.level}   Progress: {self.exp}/{self.exp_to_level}\nStatus: {status_effects}\nHealth: {self.skills['health']}\nAttack: {self.skills['attack']}    Defense: {self.skills['defense']}\nStrength: {self.skills['strength']}    Wisdom: {self.skills['wisdom']}\nAgility: {self.skills['agility']}    Luck: {self.skills['luck']}\n========== {self.name} =========="
    

        

