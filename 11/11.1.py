class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Название ресторана: ",self.restaurant_name)
        print("Тип кухни: ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")
newRestaurant=Restaurant("Чико", "Корейская")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
print("\n")
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()