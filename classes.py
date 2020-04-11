class Point:
    #initialising constructor
    def __init__(self):
        super().__init__()

    def move(self):
        print("move")

    def draw(self):
        print("draw")


#object creation of the class Point
object_of_class_point = Point()

#calling the fuction draw of the class
object_of_class_point.draw()