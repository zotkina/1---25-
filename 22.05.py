def rest():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на {self.cuisine_type} кухне Рейтинг: {self.rating} ")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def up_rating(self, new_rating):
            if 0 <= new_rating <= 5:
                self.rating = new_rating
                print(f"Рейтинг ресторана {self.restaurant_name} обновлен! Новый рейтинг: {self.rating}")
            else:
                print("Рейтинг только от 0 до 5")

    class IceCreamStand:
        def __init__(self, flavours):
            self.flavours = flavours

    newRestaurant = Restaurant("Tokio sity", "русская/американская/итальянская", 4)
    newRestaurant += IceCreamStand('фисташковое')
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.up_rating(5)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    restaurant_1 = Restaurant("Вкусно-и-Точка", "фаст-фуд", 5)
    restaurant_2 = Restaurant("Elton", "кофе", 4)
    restaurant_3 = Restaurant("Теремок", "русская", 3)

    restaurant_1.describe_restaurant()
    restaurant_2.describe_restaurant()
    restaurant_3.describe_restaurant()


rest()