#ITEMS, NOT PLAYER, WILL BE ASSIGNED INVENTORY
#player gets 2 slotS?


class Container():

    def __init__(self, item, capacity=4, max_item_weight=5):
        self.owner_item = item
        self.container = []
        self.capacity = capacity
        self.max = max_item_weight
    
    def insert(self, item):
        pass

    def withdraw(self, item):
        pass

    def use(self):
        pass