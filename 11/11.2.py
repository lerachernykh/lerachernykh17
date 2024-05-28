class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Название ресторана: ", self.restaurant_name)
        print("Тип кухни: ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")
class Restauranttwo:
    def __init__(self, restauranttwo_name, cuisine_type):
        self.restauranttwo_name=restauranttwo_name
        self.cuisine_type=cuisine_type
    def describe_restauranttwo(self):
        print("Название ресторана: ", self.restauranttwo_name)
        print("Тип кухни: ", self.cuisine_type)
    def open_restauranttwo(self):
        print("Ресторан открыт")
class Rest:
    def __init__(self, rest_name, cuisine_type):
        self.rest_name=rest_name
        self.cuisine_type=cuisine_type
    def describe_rest(self):
        print("Название ресторана: ", self.rest_name)
        print("Тип кухни: ", self.cuisine_type)
    def open_rest(self):
        print("Ресторан открыт")

newRestaurant = Restaurant("Гоголь", "Русская")
newRestaurant1 = Restauranttwo("Сделано в Китае", "Китайская")
newRestaurant2 = Rest("Фюнамбюль", "Франция")
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
print("\n")
newRestaurant1.describe_restauranttwo()
newRestaurant1.open_restauranttwo()
print("\n")
newRestaurant2.describe_rest()
newRestaurant2.open_rest()