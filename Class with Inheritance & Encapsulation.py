# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price      # 🔒 Encapsulated (private attribute)

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def get_price(self):          # Public getter method
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")


# Subclass (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)  # Inherit from Smartphone
        self.gpu = gpu

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} at high settings! 🎮")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 999)
gaming1 = GamingPhone("Asus", "ROG Phone 7", 1299, "Adreno GPU")

# Use methods
phone1.call("123-456-7890")
print("Price:", phone1.get_price())

gaming1.call("987-654-3210")
gaming1.play_game("PUBG Mobile")
print("Gaming Phone Price:", gaming1.get_price())
