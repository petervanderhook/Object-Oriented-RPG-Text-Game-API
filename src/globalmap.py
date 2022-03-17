# V = Village ( Opens Nested Map )
# M = Mountain Cave Entrance

# X = IMPASSABLE TERRAIN
# W = Water
# 0 = Plains
# 1 = Forest
# C = Cave
# S = Spawn
# P = Path
# B = Bridge
#      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15  
#    |----------------------------------------------|
#  1 | 0  0  0  0  0  W  W  0  0  0  P  0  0  0  0  |
#  2 | 0  0  0  0  0  W  P  P  P  P  P  0  0  0  0  |
#  3 | 0  0  V  P  P  B  P  0  0  0  0  0  0  0  0  |
#  4 | 0  0  0  0  0  W  P  0  0  0  X  X  X  0  0  |
#  5 | 0  0  0  0  W  W  P  0  0  X  X  X  X  X  0  |
#  6 | 0  0  0  0  W  P  P  0  0  X  X  X  X  X  0  |
#  7 | W  0  0  W  W  P  0  0  0  0  X  M  X  0  0  |
#  8 | W  W  W  W  0  P  0  0  0  0  0  0  0  0  0  |
#  9 | W  W  W  W  0  P  0  0  0  0  0  0  0  0  1  |
# 10 | W  W  W  0  P  P  P  P  P  0  1  1  1  1  1  |
# 11 | W  W  W  0  P  0  0  0  P  P  P  P  P  P  P  |
# 12 | W  W  0  0  P  0  0  0  0  1  1  C  1  1  P  |
# 13 | 0  0  0  0  P  0  0  0  0  1  1  1  1  1  V  |
# 14 | 0  0  0  0  P  V  0  0  1  1  1  1  1  1  1  |
# 15 | 0  0  0  0  0  0  0  0  1  1  1  1  1  1  1  |
#    |----------------------------------------------| 
class GlobalMap():
    
    def __init__(self):
        """Assigns tiles to a labeled list via their coordinates. 
        Generates the largest type of tiles (plains) by checking if generated tiles are already in use.
        
        Maybe will have a list of available spawn points? Or have one that is fixed? Or random depending on difficulty.
        
        """
        self.water = [[1, 6], [1, 7], [2, 6], [4, 6], [5, 6], [5, 5], [6, 5], [7, 5], [7, 4], [7, 1], [8, 1], [8, 2], [8, 3], [8, 4], [9, 1], [9, 2], [9, 3], [9, 4], [10, 1], [10, 2], [10, 3], [11, 1], [11, 2], [11, 3], [12, 1], [12, 2]]
        self.instances = [[3, 3], [14, 6], [13, 15], [7, 12], [12, 12]]
        self.bridge = [[3, 6]]
        self.impassable = [[4, 11], [4, 12], [4, 13], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [7, 11], [7, 13]]
        self.trail = [[1, 11], [2, 11], [2, 10], [2, 9], [2, 9], [2, 7], [3, 7], [3, 5], [3, 4], [4, 7], [5, 7], [6, 7], [6, 6], [7, 6], [8, 6], [9, 6], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [11, 9], [11, 10,], [11, 11], [11, 12], [11, 13], [11, 14], [11, 15], [12, 15], [11, 5], [12, 5], [13, 5], [14, 5]]
        self.forest = [[9, 15], [10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [12, 10], [12, 11], [12, 13], [12, 14], [13, 10], [13, 11], [13, 12], [13, 13], [13, 14], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [14, 15], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [15, 15]]
        plains = []
        for i in range(1, 16):
            for j in range(1, 16):
                x = [i, j]
                if x in self.water:
                    pass
                elif x in self.instances:
                    pass
                elif x in self.impassable:
                    pass
                elif x in self.trail:
                    pass
                elif x in self.forest:
                    pass
                elif x in self.bridge:
                    pass
                else: 
                    plains.append(x)
        self.plains = plains

    def check_adjacent_tiles(self, type):
        """Checks if type of tile is adjacent to your current tile. Maybe useful for items like fishing?"""
        pass

    def move(self):
        """
        Moves from one 'tile' to an adjacent one on the map. Ensures the tile is available and allows movement"""
        pass

    def enter_instance(self):
        """Enters a nested map or instance.
        """
        pass




class MapInstance(GlobalMap):
    """child class for nested maps"""
    def __init__(self):
        pass