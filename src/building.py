
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