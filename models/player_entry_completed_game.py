from models.brawler_info import BrawlerInfo
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class PlayerEntryCompletedGame:
    """
    Represents a player's entry in a completed game.

    Attributes:
        tag: The player's unique tag.
        name: The player's name.
        brawler: Information about the brawler used.
    """
    def __init__(
        self,
        tag: str,
        name: str,
        brawler: BrawlerInfo
    ):
        """
        Initialize a new PlayerEntryCompletedGame instance.

        Args:
            tag: The player's unique tag.
            name: The player's name.
            brawler: Information about the brawler used.
        """
        self.tag = tag
        self.name = name
        self.brawler = brawler

    def __str__(self) -> str:
        """
        Returns the string representation of the player entry.

        Returns:
            str: A string containing the player's name, tag, and brawler info.
        """
        return f"{self.name} ({self.tag}) - {self.brawler}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerEntryCompletedGame":
        """
        Creates a PlayerEntryCompletedGame instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerEntryCompletedGame: A new PlayerEntryCompletedGame instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player entry data, got {type(json_data)}")

        try:
            brawler_data = json_data.get("brawler")
            if not isinstance(brawler_data, dict):
                raise ParseException(f"Expected 'brawler' to be a dictionary, got {type(brawler_data)}")
            brawler = BrawlerInfo.from_json(brawler_data, client)

            return PlayerEntryCompletedGame(
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "")),
                brawler=brawler
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player entry data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player entry data: {e}")