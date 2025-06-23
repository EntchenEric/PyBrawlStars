from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class BattleBrawler:
    """
    Represents a brawler used in a battle.

    Attributes:
        id: The unique identifier of the brawler.
        name: The name of the brawler.
        power: The power level of the brawler.
        trophies: The trophy count of the brawler.
    """

    id: int
    """The unique identifier of the brawler in the game."""

    name: str
    """The name of the brawler (e.g., 'Shelly', 'Colt', 'Bull')."""

    power: int
    """The power level of the brawler (1-11)."""

    trophies: int
    """The trophy count of the brawler."""

    def __init__(
        self,
        id: int,
        name: str,
        power: int,
        trophies: int
    ):
        """
        Initialize a new BattleBrawler instance.

        Args:
            id: The unique identifier of the brawler.
            name: The name of the brawler.
            power: The power level of the brawler.
            trophies: The trophy count of the brawler.
        """
        self.id = id
        self.name = name
        self.power = power
        self.trophies = trophies

    def __str__(self) -> str:
        """
        Returns the string representation of the battle brawler.

        Returns:
            str: The brawler's name, power level, and trophies.
        """
        return f"{self.name} (Power {self.power}, {self.trophies} trophies)"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BattleBrawler":
        """
        Creates a BattleBrawler instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BattleBrawler: A new BattleBrawler instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for battle brawler data, got {type(json_data)}")

        try:
            return BattleBrawler(
                id=int(json_data.get("id", 0)),
                name=str(json_data.get("name", "")),
                power=int(json_data.get("power", 1)),
                trophies=int(json_data.get("trophies", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse battle brawler data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing battle brawler data: {e}")