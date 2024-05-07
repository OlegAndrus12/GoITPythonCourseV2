from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        # https://en.wikipedia.org/wiki/Haversine_formula
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))
    
    @staticmethod
    def get_formula():
        return "https://en.wikipedia.org/wiki/Haversine_formula"


oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
oslo.distance_to(vancouver)
print(type(oslo))


# from dataclasses import dataclass
# from typing import List

# @dataclass
# class PlayingCard:
#     rank: str
#     suit: str

# @dataclass
# class Deck:
#     cards: List[PlayingCard]

# queen_of_hearts = PlayingCard('Q', 'Hearts')
# ace_of_spades = PlayingCard('A', 'Spades')
# two_cards = Deck([queen_of_hearts, ace_of_spades])
