from models.parse_error import ParseException

from models.star_power import StarPower, from_json as star_power_from_json
from models.accessory import Accessory, from_json as accessory_from_json
from models.gear_stat import GearStat, from_json as gear_stat_from_json


class BrawlerStat:
    star_powers: list[StarPower]
    gadgets: list[Accessory]
    id: int
    rank: int
    trophies: int
    highest_trophies: int
    power: int
    gears: list[GearStat]
    name: str

    def __init__(
        self,
        star_powers: list[StarPower],
        gadgets: list[Accessory],
        id: int,
        rank: int,
        trophies: int,
        highest_trophies: int,
        power: int,
        gears: list[GearStat],
        name: str,
    ):
        self.star_powers = star_powers
        self.gadgets = gadgets
        self.id = id
        self.rank = rank
        self.trophies = trophies
        self.highest_trophies = highest_trophies
        self.power = power
        self.gears = gears
        self.name = name


def from_json(json: dict[str, str | dict[str, str]]) -> BrawlerStat:
    print("json:", json)
    try:
        BrawlerStat(
            star_powers=star_power_from_json(json.get("starPowers")),
            gadgets=accessory_from_json(json.get("gadgets")),
            id=int(json.get("id")),
            rank=int(json.get("rank")),
            trophies=int(json.get("trophies")),
            highest_trophies=int(json.get("highestTrophies")),
            power=int(json.get("power")),
            gears=gear_stat_from_json(json.get("gears")),
            name=json.get("name"),
        )
    except:
        raise ParseException()
