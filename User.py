# module for textadvzix


# represents the user
class User:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.coords = str(x) + "x" + str(y)
