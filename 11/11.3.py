class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print("Название ресторана -", self.restaurant_name, "Тип кухни -", self.cuisine_type, "Рейтинг заведения -", self.rating)
    def n_rating(self, new_rating):
        self.rating = new_rating
        print("Рейтинг обновлен на", new_rating)
    def open_restaurant(self):
        print("Ресторан открыт")

newRestaurant = Restaurant("Чико, ", "Корейская, ", 5)
newRestaurant.n_rating(5)
newRestaurant.describe_restaurant()