# module for textadvzix


# object which represents a spot on the map
class Spot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.strx = str(x)
        self.stry = str(y)

        self.passable_north = True
        self.passable_east = True
        self.passable_south = True
        self.passable_west = True

        self.view = {"n": str(),
                     "e": str(),
                     "s": str(),
                     "w": str()}
