# #1: Define a Vehicle class with the following properties and methods: 
# - `vehicle_type` 
# - `wheel_count`
# - `name` 
# - `cost` 
# - `colors` 
# - `vehicle_brand` 
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway` 
#     - `combined` 
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the class's `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_count  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. Define the properties on the class from the dict that is passed in.

dictionary1 = {
    'vehicle_type' : 'suv',
    'wheel_count' : 0,
    'name' : 'civic',
    'cost' : 10000,
    'colors' : 'black',
    'vehicle_brand' : 'honda',
    'mpg' : {
        'city' : 20,
        'highway' : 30,
        'combined' : 25
    }
}


class Vehicle:
  def __init__(self, dictionary):
    self.dictionary = dictionary
    self.vehicle_type = dictionary['vehicle_type']
    self.wheel_count = dictionary['wheel_count']
    self.name = dictionary['name']
    self.cost = dictionary['cost']
    self.colors = dictionary['colors']
    self.vehicle_brand = dictionary['vehicle_brand']
    self.mpg = dictionary['mpg']


  def get_vehicle_type(self):
    print("Vehicle type is: " + self.vehicle_type)
    return self.vehicle_type
  
  def get_vehicle_brand(self):
    print("Vehicle brand is: " + self.vehicle_brand)
    return self.vehicle_brand

  def get_vehicle_drive(self):
      if self.wheel_count < 1:
          no_wheels = "no wheels send it back to the shop"
          print(no_wheels)
          return no_wheels
      else:
          amount_wheels = "I have "  + str(self.wheel_count)  + " wheel drive"
          print(amount_wheels)
          return amount_wheels

vehicle = Vehicle(dictionary1)
vehicle.get_vehicle_type()
vehicle.get_vehicle_brand()
vehicle.get_vehicle_drive()


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following properties and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
#       otherwise return "......pop!"
class Motorcycle(Vehicle):
    def __init__(self, dictionary, button):
        super().__init__(dictionary)
        self.dictionary = dictionary
        self.wheel_count = "no wheels!"
        self.button = button
    
    def pop_wheelie(self):
        if self.wheel_count != 2:
            return False
        elif self.wheel_count == 2:
            return '......pop!'



# #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to 4
# - method: `can_drive` that should return 'Vrrooooom Vroooom'
class Car(Vehicle):
    def __init__(self, dictionary):
        super().__init__(dictionary)
        self.dictionary = dictionary
        self.wheel_count = 4
    
    def can_drive(self):
        return 'Vrrooooom Vroooom'


# #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
# - property: `wheel_count` defaults to "no wheels!"
# - method: `rev_engine` that should return 'revvvvvreeeev'
class Truck(Vehicle):
    def __init__(self, dictionary):
        super().__init__(dictionary)
        self.dictionary = dictionary
        self.wheel_count = "no wheels!"
    
    def rev_engine(self):
        return 'revvvvvreeeev'



# Commit when you finish working on these questions!