from models.star_power import StarPower
from models.gadgets import Gadgets
from models.gear_stats import GearStat

class BrawlerStat:
    gears: list[GearStat]
    trophies: int
    power: int
    trophy_change: int
    star_power: StarPower
    gadget: Gadgets
    name: str
    id: int