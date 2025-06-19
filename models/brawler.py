from models.accessory import Accessory
from models.star_power import StarPower
from typing import Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Brawler:
    """
    Represents a Brawler in the game.

    Attributes:
        gadgets: List of gadgets the brawler has.
        name: The name of the brawler.
        id: The unique identifier of the brawler.
        starPowers: List of star powers the brawler has.
    """

    gadgets: List[Accessory]
    """List of gadgets (special abilities) that this brawler has unlocked."""

    name: str
    """The name of the brawler (e.g., 'Shelly', 'Colt', 'Bull')."""

    id: int
    """The unique identifier of the brawler in the game."""

    star_powers: List[StarPower]
    """List of star powers (passive abilities) that this brawler has unlocked."""

    def __init__(
        self,
        gadgets: List[Accessory],
        name: str,
        id: int,
        star_powers: List[StarPower]
    ):
        """
        Initialize a new Brawler instance.

        Args:
            gadgets: List of gadgets the brawler has.
            name: The name of the brawler.
            id: The unique identifier of the brawler.
            star_powers: List of star powers the brawler has.
        """
        self.gadgets = gadgets
        self.name = name
        self.id = id
        self.star_powers = star_powers

    def __str__(self) -> str:
        """
        Returns the string representation of the brawler.

        Returns:
            str: The brawler's name and ID.
        """
        return f"{self.name} (ID: {self.id})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Brawler":
        """
        Creates a Brawler instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Brawler: A new Brawler instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for brawler data, got {type(json_data)}")

        try:
            gadgets_data = json_data.get("gadgets", [])
            if not isinstance(gadgets_data, list):
                raise ParseException(f"Expected 'gadgets' to be a list, got {type(gadgets_data)}")
            gadgets = [Accessory.from_json(g, client) for g in gadgets_data if isinstance(g, dict)]

            star_powers_data = json_data.get("starPowers", [])
            if not isinstance(star_powers_data, list):
                raise ParseException(f"Expected 'starPowers' to be a list, got {type(star_powers_data)}")
            star_powers = [StarPower.from_json(sp, client) for sp in star_powers_data if isinstance(sp, dict)]

            return Brawler(
                gadgets=gadgets,
                name=str(json_data.get("name", "")),
                id=int(json_data.get("id", 0)),
                star_powers=star_powers
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse brawler data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing brawler data: {e}")