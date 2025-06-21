from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class PlayerClub:
    """
    Represents a player's club information.

    Attributes:
        tag: The club's unique tag.
        name: The name of the club.
    """
    def __init__(
        self,
        tag: str,
        name: str
    ):
        """
        Initialize a new PlayerClub instance.

        Args:
            tag: The club's unique tag.
            name: The name of the club.
        """
        self.tag = tag
        self.name = name

    def __str__(self) -> str:
        """
        Returns the string representation of the player's club.

        Returns:
            str: The club's name and tag.
        """
        return f"{self.name} ({self.tag})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerClub":
        """
        Creates a PlayerClub instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerClub: A new PlayerClub instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player club data, got {type(json_data)}")

        try:
            return PlayerClub(
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", ""))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player club data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player club data: {e}")