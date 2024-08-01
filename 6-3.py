class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "しゃり"

    def show_attributes(self):
        print(f"top: {self.top}, base: {self.base}, category: {self.category}")


class Maguro(Nigiri):
    top = "まぐろ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print(f"price: {self.price}円")

    def show_one_dish_price(self, num_nigiri=2):
        result = self.price * num_nigiri
        print(f"1皿({num_nigiri}かん)の値段: {result}円")

m5 = Maguro()
m5.show_attributes()
m5.show_one_dish_price()
