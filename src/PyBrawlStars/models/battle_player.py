from .battle_brawler import BattleBrawler
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class BattlePlayer:
    """
    Represents a player in a battle.

    Attributes:
        tag: The player's unique tag.
        name: The player's name.
        brawler: The brawler used by the player in the battle.
    """

    tag: str
    """The player's unique tag (e.g., '#2qquclvll')."""

    name: str
    """The player's in-game name."""

    brawler: BattleBrawler
    """The brawler used by the player in this battle."""

    def __init__(
        self,
        tag: str,
        name: str,
        brawler: BattleBrawler
    ):
        """
        Initialize a new BattlePlayer instance.

        Args:
            tag: The player's unique tag.
            name: The player's name.
            brawler: The brawler used by the player in the battle.
        """
        self.tag = tag
        self.name = name
        self.brawler = brawler

    def __str__(self) -> str:
        """
        Returns the string representation of the battle player.

        Returns:
            str: The player's name, tag, and brawler.
        """
        return f"{self.name} ({self.tag}) - {self.brawler.name}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BattlePlayer":
        """
        Creates a BattlePlayer instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BattlePlayer: A new BattlePlayer instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for battle player data, got {type(json_data)}")

        try:
            brawler_data = json_data.get("brawler")
            if not isinstance(brawler_data, dict):
                raise ParseException(f"Expected 'brawler' to be a dictionary, got {type(brawler_data)}")
            brawler = BattleBrawler.from_json(brawler_data, client)

            return BattlePlayer(
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "")),
                brawler=brawler
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse battle player data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing battle player data: {e}")