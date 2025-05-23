from models.accessory import Accessory
from models.star_power import StarPower

class Brawler:
    gadgets: list[Accessory]
    name: str
    id: int
    starPowers: list[StarPower]