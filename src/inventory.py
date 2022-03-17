#ITEMS, NOT PLAYER, WILL BE ASSIGNED INVENTORY
#player gets 2 slotS?
from item import Item


class Container():

    def __init__(self, item, capacity=4, max_item_weight=5):
        self.owner_item = item
        self.container = []
        self.capacity = capacity
        self.max = max_item_weight
    
    def insert(self, thing):
        if isinstance(thing, Item):
            if len(self.container) < self.capacity:
                self.container.append(thing)
    
    def withdraw(self, item):
        pass

    def use(self):
        pass