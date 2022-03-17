
class Item():

    def __init__(self, name, value=0, weight=0, effect=[]):
        self.name = name
        self.value = value
        self.weight = weight
        self.effect = effect
    

    def rename(self):
        pass

    def __repr__(self) -> str:
        return self.name

    def improve(self):
        pass

    def sell(self, char):
        pass

    def discard(self):
        pass

class Consumeable(Item):

    def __init__(self, name, value=0, weight=0, effect=[], boost=None):
        pass



class Gear(Item):
        
    def __init__(self, name, value=0, weight=0, effect=[], stats=[0, 0, 0, 0, 0, 0], slot="trinket"):
        self.name = name
        self.value = value
        self.weight = weight
        self.effect = effect
        self.stats = stats
        self.slot = slot
        self.worn = False
    

    def equip(self):
        pass

    def unequip(self):
        pass
