# shallow copy

xs = [[1,2.3], [4,5,6], [7,8,9]]

class Point:
    """ Points class represents and manipulate x,y coords """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    def __repr__(self):

        return (Rectangle({self.topleft}, {self.bottomright}))
rect = Rectangle(Point(0,1),Point(5,6))
srect = copy.copy(rect)