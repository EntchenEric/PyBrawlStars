from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class StarPower:
    """
    Represents a Star Power in the game.

    Attributes:
        name: The name of the star power.
        id: The unique identifier of the star power.
    """
    def __init__(self, name: str, id: int):
        """
        Initialize a new StarPower instance.

        Args:
            name: The name of the star power.
            id: The unique identifier of the star power.
        """
        self.name = name
        self.id = id

    def __str__(self) -> str:
        """
        Returns the string representation of the star power.

        Returns:
            str: The star power's name and ID.
        """
        return f"{self.name} (ID: {self.id})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "StarPower":
        """
        Creates a StarPower instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            StarPower: A new StarPower instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for star power data, got {type(json_data)}")

        try:
            return StarPower(
                name=str(json_data.get("name", "")),
                id=int(json_data.get("id", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse star power data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing star power data: {e}")