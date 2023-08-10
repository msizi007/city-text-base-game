
# CREATING CLASS FOR ITEMS

class Item:
    def __init__(self, name: str, price: float, item_type: str, 
                 rate: float, bar_code: int):
        self.name = name
        self.price = price
        self.item_type = item_type
        self.rate = rate
        self.bar_code = bar_code


Doritos_Snacks = Item(name="Doritos Snacks", 
                      price=22, item_type="food", rate=8, bar_code=12)
Pure_Water = Item(name="Pure Water",
                   price=10, item_type="water", rate=10, bar_code=1)

