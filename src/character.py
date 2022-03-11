

class Character():
    
    def __init__(self, name):
        self.name = name
        self.skillpoints = 4
        self.level = 1
        self.skills = { "attack": 3, "defense": 3, "wisdom": 3, "agility": 3, "luck": 3, "health": 10}
        self.exp = 0
        self.exp_to_level = 69
        self.status = []


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
    
    def __repr__(self):
        return f"========== {self.name} ==========\nLevel: {self.level}   Progress: {self.exp}/{self.exp_to_level}\nStatus: {self.status}\nAttack: {self.skills['attack']}    Defense: {self.skills['defense']}\nWisdom: {self.skills['wisdom']}    Agility: {self.skills['agility']}\nHealth: {self.skills['health']}    Luck: {self.skills['luck']}\n========== {self.name} =========="
    

        

