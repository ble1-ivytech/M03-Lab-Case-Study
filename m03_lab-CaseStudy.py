'''
Bryant Le
m03_lab-CaseStudy.py
This program allows the user to enter their vehicle and its details, and output all information to an organized list.
'''

# Vehicle as an Object, will be used for Car class to be inherited.


class Vehicle():
    def __init__(self, c_type):
        self.c_type = c_type

    def __str__(self):
        result = "Vehicle Type: " + self.c_type + '\n'
        return result

# Car as an Object, inherits the Vehicle class, and used as basis for organizing details to a list


class Car(Vehicle):
    def __init__(self, c_type, year, make, model, doors, roof):
        super().__init__(c_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        result = "Vehicle Type: " + self.c_type + '\n'
        result += "Year: " + self.year + '\n'
        result += "Make: " + self.make + '\n'
        result += "Model: " + self.model + '\n'
        result += "Number of Doors: " + self.doors + '\n'
        result += "Type of Roof: " + self.roof + '\n'
        return result


# User enter details
vehicle_type = input("Enter the type of vehicle you own: ")
vehicle_year = input("Enter the release year of your vehicle: ")
vehicle_make = input("Enter your manufacturer's name: ")
vehicle_model = input("Enter the model name of your vehicle: ")
vehicle_doors = input("Enter the amount of doors on your vehicle: ")
vehicle_roof = input("Enter the type of roof on your vehicle: ")

# Car details are organized to a list refering to Car.__str__
car_details = Car(str(vehicle_type), str(vehicle_year), str(
    vehicle_make), str(vehicle_model), str(vehicle_doors), str(vehicle_roof))

# Outputs information
print(car_details)
