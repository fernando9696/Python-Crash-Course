#  Class example using firearms
# Firearms have brand, caliber, action, longgun/handgun, color, capacity, features

class Gun:

    def __init__(self, brand, model, caliber, capacity, type, color, action):
        self.brand = brand
        self.model = model
        self.caliber = caliber
        self.capacity = capacity
        self.type = type
        self.color = color
        self.action = action

# Can also add weight, serial number, finish, barrel length, dimensions, rifling, material, length of pull, sights

    def description(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Caliber: {self.caliber}")
        print(f"Action: {self.action}")
        print(f"Capacity: {self.capacity}")
        print(f"Type: {self.type}")
        print(f"Color: {self.color}")
        print('\n')

backpack = Gun('Ruger', '57', '5.7 x 28mm', 20, 'Handgun', 'Black',  'Semi-Automatic')
range = Gun('Ruger', 'Mark IV', '.22lr', 10, 'Handgun', 'Black', 'Semi-Automatic')
carry = Gun('Glock', '43', '9 x 19mm', 6, 'Handgun', 'Black', 'Semi-Automatic')
side = Gun('Springfield Armory', '1911 Loaded', '.45 ACP', 7, 'Handgun', 'Black', 'Semi-Automatic')
home = Gun('Remington', '870 Express Tactical', '12ga', 6, 'Shotgun', 'Black', 'Pump-Action')
backpack2 = Gun('Aero-Precision', 'M4E1 (AR-15 style)', '.300 BLK', '20/30', 'Handgun', 'Black', 'Semi-Automatic Gas Impingement')
truck = Gun('AeroPrecision', 'AR-15', '5.56 x 45mm NATO', 30, 'Rifle', 'Black', 'Semi-Automatic Gas Impingement')
range_day = Gun('Henry', 'Classic', '.22lr', 15, 'Rifle', 'Black and Walnut', 'Lever Action')
hunting = Gun('Savage Arms', 'Axis', '.30-06 Springfield', 4, 'Rifle', 'Black', 'Bolt Action')
revolution = Gun('Century Arms', 'C39V2 (AK)', '7.62 x 39mm Soviet', 30, 'Rifle', 'Black and Walnut', 'Semi-Automatic Gas Piston ')

backpack.description()
backpack2.description()
range.description()
range_day.description()
carry.description()
side.description()
truck.description()
hunting.description()
revolution.description()
home.description()
