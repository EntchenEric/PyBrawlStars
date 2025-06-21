from .parse_error import ParseException
from .star_power import StarPower
from .accessory import Accessory
from .gear_stat import GearStat
from typing import Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import BSClient


class BrawlerStat:
    """
    Represents statistics for a specific brawler.

    Attributes:
        star_powers: List of star powers unlocked for this brawler.
        gadgets: List of gadgets unlocked for this brawler.
        id: The unique identifier of the brawler.
        rank: The current rank of the brawler.
        trophies: The current number of trophies with this brawler.
        highest_trophies: The highest number of trophies achieved with this brawler.
        power: The power level of the brawler.
        gears: List of gears equipped on this brawler.
        name: The name of the brawler.
    """

    star_powers: List[StarPower]
    """List of star powers unlocked for this brawler."""

    gadgets: List[Accessory]
    """List of gadgets unlocked for this brawler."""

    id: int
    """The unique identifier of the brawler."""

    rank: int
    """The current rank of the brawler."""

    trophies: int
    """The current number of trophies with this brawler."""

    highest_trophies: int
    """The highest number of trophies achieved with this brawler."""

    power: int
    """The power level of the brawler."""

    gears: List[GearStat]
    """List of gears equipped on this brawler."""

    name: str
    """The name of the brawler."""

    def __init__(
        self,
        star_powers: List[StarPower],
        gadgets: List[Accessory],
        id: int,
        rank: int,
        trophies: int,
        highest_trophies: int,
        power: int,
        gears: List[GearStat],
        name: str,
    ):
        """
        Initialize a new BrawlerStat instance.

        Args:
            star_powers: List of star powers unlocked for this brawler.
            gadgets: List of gadgets unlocked for this brawler.
            id: The unique identifier of the brawler.
            rank: The current rank of the brawler.
            trophies: The current number of trophies with this brawler.
            highest_trophies: The highest number of trophies achieved with this brawler.
            power: The power level of the brawler.
            gears: List of gears equipped on this brawler.
            name: The name of the brawler.
        """
        self.star_powers = star_powers
        self.gadgets = gadgets
        self.id = id
        self.rank = rank
        self.trophies = trophies
        self.highest_trophies = highest_trophies
        self.power = power
        self.gears = gears
        self.name = name

    def __str__(self) -> str:
        """
        Returns the string representation of the brawler stats.

        Returns:
            str: A string containing the brawler name, power level, and trophy count.
        """
        return f"{self.name} (Power {self.power}, {self.trophies} trophies, Rank {self.rank})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BrawlerStat":
        """
        Creates a BrawlerStat instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BrawlerStat: A new BrawlerStat instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for brawler stat data, got {type(json_data)}")

        try:
            star_powers_data = json_data.get("starPowers", [])
            if not isinstance(star_powers_data, list):
                raise ParseException(f"Expected 'starPowers' to be a list, got {type(star_powers_data)}")
            star_powers = [StarPower.from_json(sp, client) for sp in star_powers_data if isinstance(sp, dict)]

            gadgets_data = json_data.get("gadgets", [])
            if not isinstance(gadgets_data, list):
                raise ParseException(f"Expected 'gadgets' to be a list, got {type(gadgets_data)}")
            gadgets = [Accessory.from_json(g, client) for g in gadgets_data if isinstance(g, dict)]

            gears_data = json_data.get("gears", [])
            if not isinstance(gears_data, list):
                raise ParseException(f"Expected 'gears' to be a list, got {type(gears_data)}")
            gears = [GearStat.from_json(gear, client) for gear in gears_data if isinstance(gear, dict)]

            return BrawlerStat(
                star_powers=star_powers,
                gadgets=gadgets,
                id=int(json_data.get("id", 0)),
                rank=int(json_data.get("rank", 0)),
                trophies=int(json_data.get("trophies", 0)),
                highest_trophies=int(json_data.get("highestTrophies", 0)),
                power=int(json_data.get("power", 0)),
                gears=gears,
                name=str(json_data.get("name", ""))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse brawler stat data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing brawler stat data: {e}")
