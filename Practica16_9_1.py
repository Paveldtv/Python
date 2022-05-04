class Rectangle:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def get_area(self):
       return self.width*self.height
    def __str__(self):
        return f"Rectangle: {self.x},{self.y},{self.width},{self.height}"
rectangle_1=Rectangle(5,10,50,100)
print(rectangle_1)
print(f"S={rectangle_1.get_area()}")