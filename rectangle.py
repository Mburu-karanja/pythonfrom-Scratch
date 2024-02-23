#class rectangle
#variables length and width
#method area retun area
#method perimeter return
#call the method

class  rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width =width
    def area(self):
        area_1=self.length*self.width
        return area_1
    def perimeter(self):
        perimeter_1=self.length + self.width
        return perimeter_1
rectangle=rectangle(float(input("enter length:")), float(input("enter width:")))
print("area :",rectangle.area())
print("perimeter :",rectangle.perimeter())
