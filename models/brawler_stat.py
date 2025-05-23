from models.star_power import StarPower
from models.gadgets import Gadgets
from models.gear_stats import GearStat

class BrawlerStat:
    star_powers: list[StarPower]
    gadgets: list[Gadgets]
    id: int
    rank: int
    trophies: int
    highest_trophies: int
    power: int
    gears: list[GearStat]
    name: str