
class Ability:
    def __init__(self, name: str, affects: dict, time: int):
        self.name = name
        self.affects = affects
        self.time = time

    def use(self):
        pass

Freeze __init__(self): pass

