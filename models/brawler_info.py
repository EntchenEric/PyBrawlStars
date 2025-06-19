from models.star_power import StarPower
from models.accessory import Accessory
from models.gear_stat import GearStat
from typing import Any, TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class BrawlerInfo:
    """
    Represents detailed information about a brawler.

    Attributes:
        gears: List of gear stats for the brawler.
        trophies: Current trophy count.
        power: Power level of the brawler.
        trophy_change: Change in trophies from the last match.
        star_power: The equipped star power.
        gadget: The equipped gadget.
        name: The brawler's name.
        id: The brawler's unique identifier.
    """

    gears: List[GearStat]
    """List of gear stats for the brawler, containing information about equipped gears and their levels."""

    trophies: int
    """Current trophy count for this brawler."""

    power: int
    """Power level of the brawler (1-11)."""

    trophy_change: int
    """Change in trophies from the last match (can be positive or negative)."""

    star_power: Optional[StarPower]
    """The currently equipped star power, or None if no star power is equipped."""

    gadget: Optional[Accessory]
    """The currently equipped gadget, or None if no gadget is equipped."""

    name: str
    """The brawler's name (e.g., 'Shelly', 'Colt', 'Bull')."""

    id: int
    """The brawler's unique identifier in the game."""

    def __init__(
        self,
        gears: List[GearStat],
        trophies: int,
        power: int,
        trophy_change: int,
        star_power: Optional[StarPower],
        gadget: Optional[Accessory],
        name: str,
        id: int
    ):
        """
        Initialize a new BrawlerInfo instance.

        Args:
            gears: List of gear stats for the brawler.
            trophies: Current trophy count.
            power: Power level of the brawler.
            trophy_change: Change in trophies from the last match.
            star_power: The equipped star power.
            gadget: The equipped gadget.
            name: The brawler's name.
            id: The brawler's unique identifier.
        """
        self.gears = gears
        self.trophies = trophies
        self.power = power
        self.trophy_change = trophy_change
        self.star_power = star_power
        self.gadget = gadget
        self.name = name
        self.id = id

    def __str__(self) -> str:
        """
        Returns the string representation of the brawler info.

        Returns:
            str: A string containing the brawler's name, power level, and trophies.
        """
        return f"{self.name} (Power {self.power}, {self.trophies} trophies)"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BrawlerInfo":
        """
        Creates a BrawlerInfo instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BrawlerInfo: A new BrawlerInfo instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for brawler info data, got {type(json_data)}")

        try:
            gears_data = json_data.get("gears", [])
            if not isinstance(gears_data, list):
                raise ParseException(f"Expected 'gears' to be a list, got {type(gears_data)}")
            gears = [GearStat.from_json(g, client) for g in gears_data if isinstance(g, dict)]

            star_power_data = json_data.get("starPower")
            star_power = StarPower.from_json(star_power_data, client) if isinstance(star_power_data, dict) else None

            gadget_data = json_data.get("gadget")
            gadget = StarPower.from_json(gadget_data, client) if isinstance(gadget_data, dict) else None

            return BrawlerInfo(
                gears=gears,
                trophies=int(json_data.get("trophies", 0)),
                power=int(json_data.get("power", 0)),
                trophy_change=int(json_data.get("trophyChange", 0)),
                star_power=star_power,
                gadget=gadget,
                name=str(json_data.get("name", "")),
                id=int(json_data.get("id", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse brawler info data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing brawler info data: {e}")