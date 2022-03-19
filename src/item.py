
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



class Gear(Item):#                                                Atk Str Def Wis Agi Lck Hp
    """Gear/equipment child class."""
    def __init__(self, name, capacity=0, value=0, weight=0, effect=[], stats={'attack': 0, 'strength': 0, 'defense': 0, 'wisdom': 0, 'agility': 0, 'luck': 0, 'health': 0}, slot="trinket"):
        self.name = name
        self.capacity = capacity
        self.value = value
        self.weight = weight
        self.effect = effect
        self.stats = stats
        self.slot = slot
        self.worn = False
    
    def __repr__(self):
        return str(self.name)
