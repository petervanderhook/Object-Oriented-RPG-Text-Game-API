#ITEMS, NOT PLAYER, WILL BE ASSIGNED INVENTORY
#player gets 2 slotS?
from item import Item


class Container():

    def __init__(self, item: Item, capacity=4, max_item_weight=5):
        """
        Constructor for Container Object

        Args:
        item = Item that actually has the space, the container itself is this item
        capacity = Maximum amount of item objects stored in the container
        max_item_weight = Maximum weight of the container or items in container? 50/50 on whether I keep this
        
        Attributes:
        owner_item = item arg
        stored = list of items currently stored in container
        capacity = (int) max slots of storage available
        current_weight = Total weight of all items including item itself

        """
        self.owner_item = item
        self.stored = []
        self.capacity = capacity
        self.current_weight = item.weight
        self.max = max_item_weight
    
    def insert(self, thing):
        if isinstance(thing, Item):
            if len(self.container) < self.capacity:
                self.container.append(thing)

    
    def withdraw(self, item):
        pass

    def use(self):
        pass