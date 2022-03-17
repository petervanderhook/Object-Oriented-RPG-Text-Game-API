class Village():
    
    def __init__(self, name, buildings, map):
        self.name = name
        self.buildings = buildings
        self.map = map

    def move(self):
        pass

    def exit(self):
        pass

    def get_buildings(self):
        return_string = "Buildings in this town:\n" + str(self.buildings[0])
        if len(self.buildings) > 1:
            for i in range(1, len(self.buildings)):
                return_string += f", {self.buildings[i]}" 
        return print(return_string)

    def __repr__(self) -> str:
        return "Village: " + str(self.name)

    def enter_building(self, building):
        pass
