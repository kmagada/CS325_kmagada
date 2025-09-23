#SRP

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email

#    def save_to_database(self):
#        print("Saving to database")
#    def send_email(self):
#        print("Sending email to", self.email)
#    def generate_report(self):
#        return "Report"
    
class UserDatabase:
    def save(self, user):
        print("Saving user to database")
    def save_to_cloud(self, user):
        print("Saving user to cloud")

class EmailService:
    def send(self, email, message):
        print("Sending email to", email)

class UserGenerateReport:
    def generate(self, user):
        print("Report")

"""
class Shape:
    def __init__ (self, shape_type, **kwargs):
        self.shape_type = shape_type
        if shape_type == "rectangle":
            self.width = kwargs("width")
            self.height = kwargs("height")
        elif shape_type == "circle":
            self.radius = kwargs("radius")

class AreaCalculator:
    def calculate_area(self, shape):
        total_area = 0
        for shape in shapes:
            if shape.shape_type == "rectangle":
                total_area += shape.width * shape.height
                
            elif shape.shape_type == "circle":
                total_area += 3.14 * shape.radius * shape.radius
        return total_area
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Vehicle:
    def acc(self):
        raise NotImplementedError
    def brake(self):
        raise NotImplementedError
    def turn(self):
        raise NotImplementedError
    def fly(self):
        raise NotImplementedError

class Bicylce(Vehicle):
    def acc(self):
        pass
    def brake(self):
        pass
    def turn(self, direction):
        pass
    """
    def fly(self):
        raise Exception("Bicycles can't fly")
    """