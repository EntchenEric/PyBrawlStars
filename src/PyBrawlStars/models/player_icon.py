from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class PlayerIcon:
    """
    Represents a player's icon in the game.

    Attributes:
        id: The unique identifier of the icon.
    """

    id: int
    """The unique identifier of the icon that represents the player's profile picture."""

    def __init__(self, id: int):
        """
        Initialize a new PlayerIcon instance.

        Args:
            id: The unique identifier of the icon.
        """
        self.id = id

    def __str__(self) -> str:
        """
        Returns the string representation of the player icon.

        Returns:
            str: The icon's ID.
        """
        return f"Icon #{self.id}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerIcon":
        """
        Creates a PlayerIcon instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerIcon: A new PlayerIcon instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player icon data, got {type(json_data)}")

        try:
            icon_id = json_data.get("id")
            if icon_id is None:
                raise ParseException("Missing 'id' field in player icon JSON data")

            return PlayerIcon(id=int(icon_id))
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player icon data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player icon data: {e}")