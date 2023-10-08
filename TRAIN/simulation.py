# SIMULATE MATCHES

import pygame

class Club:
    def __init__(self, fullname: str, shortname: str, players: list=[]):
        self.fullname = fullname
        self.shortname = shortname
        self.players = players

    def add_player(self, player):
        self.players.append(player)


class Player:
    def __init__(self, fullname: str, average: int):
        self.fullname = fullname
        self.average = average


Liverpool = Club(fullname="Liverpool FC", shortname="LFC")
ManUtd = Club(fullname="Manchaster City", shortname="MCH")
ManCity = Club(fullname="Manchaster United", shortname="MTD")
Arsenal = Club(fullname="Arsenal FC", shortname="ASN")


VirginVanDyk = Player(fullname="Virgil Van Dyk", average=8)
TonniCliff = Player(fullname="Tonni Cliff", average=73)