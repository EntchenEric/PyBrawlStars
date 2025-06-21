from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass

from .brawler_info import BrawlerInfo

class MatchTeamPlayer:
    """
    Represents a player in a match team.

    Attributes:
        tag: The player's unique tag.
        name: The player's name.
        brawler_id: The ID of the brawler being used.
    """

    tag: str
    """The player's unique tag (e.g., '#2qquclvll')."""

    name: str
    """The player's in-game name."""

    brawler_id: int
    """The unique identifier of the brawler being used by the player in this match."""

    def __init__(
        self,
        tag: str,
        name: str,
        brawler_id: int
    ):
        """
        Initialize a new MatchTeamPlayer instance.

        Args:
            tag: The player's unique tag.
            name: The player's name.
            brawler_id: The ID of the brawler being used.
        """
        self.tag = tag
        self.name = name
        self.brawler_id = brawler_id

    def __str__(self) -> str:
        """
        Returns the string representation of the match team player.

        Returns:
            str: The player's name and tag.
        """
        return f"{self.name} ({self.tag})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "MatchTeamPlayer":
        """
        Creates a MatchTeamPlayer instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            MatchTeamPlayer: A new MatchTeamPlayer instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for match team player data, got {type(json_data)}")

        try:
            return MatchTeamPlayer(
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "")),
                brawler_id=int(json_data.get("brawlerId", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse match team player data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing match team player data: {e}")