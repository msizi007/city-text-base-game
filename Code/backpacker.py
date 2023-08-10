# MODULE FOR MAKING ITEMS AND WEIGHT THEM
# E.G "Doritos snacks": {"Price": R28.75, "Hunger_rate": 7, "Energy_rate": 8}

BACKPACK = []

class BackPack:
    def __init__(self):
        self.backpack = BACKPACK

    def add_item(self, item):
        self.backpack.append(item)
        self.update()

    def add_items(self, items: list):
        for t in items:
            self.backpack.append(t)
        self.update()

    def update(self):
        global BACKPACK
        BACKPACK = self.backpack

    def remove_item(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            print("-1 item removed")
            self.update()

    def remove_items(self, items):
        num_of_items = 0
        for t in items:
            if t in self.backpack:
                self.backpack.remove(t)
                num_of_items +=1
        print(f"-{num_of_items} items removed")
        self.update()

    def check_items(self):
        for item in self.backpack:
            print(item)