import turtle as t
import random

class Tree():
    """This is a class for generating recursive trees using turtle"""

    def __init__(self):
        """The constructor for Tree class"""
        self.leafColours = ["#91ff93", "#b3ffb4", "#d1ffb3", "#99ffb1", "#d5ffad"]
        t.bgcolor("#abd4ff")
        t.penup()
        t.sety(-375)
        t.pendown()
        t.color("#5c3d00")
        t.pensize(2)
        t.left(90)
        t.forward(100)  # larger trunk
        t.speed(0)
        self.rootPos = t.position()


    def __drawHelp(self, size, pos):
        """
        The private helper method to draw the tree.

        Parameters:
            size (int): How large the tree is to be.
            pos (int): The starting position of the root.
        """
        if(size < 20):
            if(size % 2 == 0):
                 # let's only dot about every second one
                t.dot(50, random.choice(self.leafColours))
            return
        elif(size < 50):
            t.dot(50, random.choice(self.leafColours))

        # inorder traversial
        t.penup()
        t.setposition(pos)
        t.pendown()
        t.forward(size)
        thisPos = t.position()
        thisHeading = t.heading()
        size = size - random.randint(10, 20)
        t.setheading(thisHeading)
        t.left(25)
        self.__drawHelp(size, thisPos)
        t.setheading(thisHeading)
        t.right(25)
        self.__drawHelp(size, thisPos)


    def draw(self, size):
        """
        The method to draw the tree.

        Parameters:
            size (int): How large the tree is to be.
        """
        self.__drawHelp(size, self.rootPos)



def main():
    tree = Tree()
    tree.draw(125)
    t.hideturtle()

    input("Press enter to terminate program: ")


if __name__ == '__main__':
    main()
