# Example of a class and creating an instance
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"This restaurant serves mainly {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

restaurant = Restaurant('Salerno\'s', 'Italian')

restaurant.describe_restaurant()

restaurant.open_restaurant()
