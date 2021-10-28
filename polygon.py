# Given is a "Polygon" class with functions: "inputSides", "dispSides" and "shapeType". 
# Your task is to create a child class Square that inherits from "Polygon". 
# Also, define a function "findArea" for the "Square" Class to calculate the area of the swuare 
# with given sides. Finally, in the "Square" class, 
# override the "shapeType" function to print in respective to it.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
    
    def shapeType(self):
        print("This is a Polygon")

class Square(Polygon):
    def __init__(self):
        super(4)

    def inputSides(self):
        size = float(input("Enter square size length:  "))
        self.sides = [ size for i in range(self.n)]
    
    def findArea(self, ):
        area = self.sides[0] ** 2
        print(f"Area: ${area}")
    
    def shapeType(self):
        print("This is a Square")