from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class PlayerEntry:
    """
    Represents a player entry in a match or event.

    Attributes:
        tag: The player's unique tag.
        side: The side/team the player is on (0 or 1).
    """

    tag: str
    """The player's unique tag (e.g., '#2qquclvll')."""

    side: int
    """The side/team the player is on (0 or 1)."""

    def __init__(
        self,
        tag: str,
        side: int
    ):
        """
        Initialize a new PlayerEntry instance.

        Args:
            tag: The player's unique tag.
            side: The side/team the player is on.
        """
        self.tag = tag
        self.side = side

    def __str__(self) -> str:
        """
        Returns the string representation of the player entry.

        Returns:
            str: A string containing the player tag and side.
        """
        return f"{self.tag} (Side {self.side})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerEntry":
        """
        Creates a PlayerEntry instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerEntry: A new PlayerEntry instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player entry data, got {type(json_data)}")

        try:
            return PlayerEntry(
                tag=str(json_data.get("tag", "")),
                side=int(json_data.get("side", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player entry data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player entry data: {e}")