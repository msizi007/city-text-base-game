# imports
from items import *

ITEMS_DICT = [Doritos_Snacks, Pure_Water]


class Shopping:
    def __init__(self, money):
        self.total = 0
        self.money = money
        self.shopping_cart = []

    def start_shopping(self):
        num_of_products = 0
        for i, product in enumerate(ITEMS_DICT, start=1):
            for item, attr in product.items():
                print(f"{i}\t{item}\t{attr.get('PRICE')}")
                num_of_products += 1

        item_chosen = 1

        while item_chosen != 0:
            print("TYPE PRODUCT NUMBER TO BUY OR 0 TO FINISH")
            item_chosen = int(input("::> "))
            if 1 <= item_chosen <= num_of_products:
                item_chosen = ITEMS_DICT[item_chosen-1]
                self.shopping_cart.append(item_chosen)

        print(self.calculate_total())
        self.checkout(self.money)

    def calculate_total(self):
        if not self.shopping_cart:
            return "TOTAL: R0.00"
        
        for product in self.shopping_cart:
            for _, attr in product.items():
                self.total += attr.get("PRICE")

        return f"TOTAL: R{self.total}"

    def checkout(self, money):
        if money >= self.total:
            money -= self.total
            print("TANK YOU FOR SHOPPING!")
            print(f"CHANGE: R{money}")
        else:
            print(F"Total price is R{self.total} which is more than what you have!")
                        

Shop = Shopping(25)
Shop.start_shopping()
