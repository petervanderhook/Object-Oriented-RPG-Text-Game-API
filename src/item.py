
class Item():
    """Default 'basic' item class with the basic functions"""

    def __init__(self, name, value=0, weight=0, effect=[]):
        """Constructor for a basic item."""
        self.name = name
        self.value = value
        self.weight = weight
        self.effect = effect
    

    def rename(self):
        """Lets you give a custom name to an item? Maybe should only be available for equipment"""
        pass

    def __repr__(self) -> str:
        """Dunder method, returns the name of the item if you want to print the object."""
        return self.name

    def improve(self):
        """Improves an item (also maybe only for gear or consumables, not sure.)"""
        pass

    def sell(self, char):
        """Sell the item to the store, basically this will give you gold and discard? Is this necessary method or extra?"""
        pass



class Consumeable(Item):
    """Consumeable item child class."""

    def __init__(self, name, value=0, weight=0, effect=[], boost=None):
        pass



class Gear(Item):
    """Gear/equipment child class."""
    def __init__(self, name, value=0, weight=0, effect=[], stats=[0, 0, 0, 0, 0, 0], slot="trinket"):
        self.name = name
        self.value = value
        self.weight = weight
        self.effect = effect
        self.stats = stats
        self.slot = slot
        self.worn = False
    

    def equip(self):
        """Equip the item. Checks if the slot is currently in use."""
        pass

    def unequip(self):
        """unequips item. Checks that you have enough space for the item in your containers."""
        pass
