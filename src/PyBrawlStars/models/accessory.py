from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Accessory:
    """
    Represents an accessory (gadget) in the game.

    Attributes:
        name: The name of the accessory.
        id: The unique identifier of the accessory.
    """
    def __init__(self, name: str, id: int):
        """
        Initialize a new Accessory instance.

        Args:
            name: The name of the accessory.
            id: The unique identifier of the accessory.
        """
        self.name = name
        self.id = id

    def __str__(self) -> str:
        """
        Returns the string representation of the accessory.

        Returns:
            str: The accessory's name and ID.
        """
        return f"{self.name} (ID: {self.id})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Accessory":
        """
        Creates an Accessory instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Accessory: A new Accessory instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for accessory data, got {type(json_data)}")

        try:
            return Accessory(
                name=str(json_data.get("name", "")),
                id=int(json_data.get("id", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse accessory data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing accessory data: {e}")