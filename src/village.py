from src.building import Building
#   X X X X X X X X    *North West Village*
#   X X ^ X E X X X    E = Exit
#   X X 0 X 0 M X X    X = Impassable
#   X E 0 0 0 0 E X    T = Tavern/Inn
#   X X 0 X 0 T X X    M = Market  
#   X B 0 X E X X X    ^ = Village Leader
#   X X X X X X X X    0 = Roads
class Village():
    
    def __init__(self, name, buildings, map):
        """Constructor for the village. More to do"""
        self.name = name
        self.buildings = buildings
        self.map = map

    def move(self):
        """Will let you move inside the village? Maybe unecessary.
        """
        pass

    def exit(self, orientation='E'):
        """Exits village and goes back to main map. Will need to determine adj tile to spit the player onto."""
        pass

    def get_buildings(self):
        """Gets a list of building names in the town with their building type"""
        return_string = "Buildings in this town:\n" + str(self.buildings[0])
        if len(self.buildings) > 1:
            for i in range(1, len(self.buildings)):
                return_string += f", {self.buildings[i]}" 
        return print(return_string)

    def __repr__(self) -> str:
        """Dunder method, prints the village name when you try to print the object"""
        return "Village: " + str(self.name)

    def enter_building(self, building: Building):
        """Enters a custom loop for the specific building. Building as parameter and then determine how function should work via the building type."""
        pass


