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

    def exit(self):
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

    def enter_building(self, building):
        """Enters a custom loop for the specific building. Building as parameter and then determine how function should work via the building type."""
        pass



class Building():

    def __init__(self, name, building_type="inn", store_inventory=[], npcs_here=[]):
        """Building has npcs inside + store inventory if available."""
        self.name = name
        self.type = building_type

    def __repr__(self):
        """Prints the name of the building and it's type. Will be used in the village function to print list of buildings."""
        return "Name: " + str(self.name) + " | Type: " + str(self.type)
    

    def shop_instance(self):
        """Shop loop when you are trying to purchase from a building."""
        pass