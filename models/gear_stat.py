from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class GearStat:
    """
    Represents a gear's statistics.

    Attributes:
        name: The name of the gear.
        id: The unique identifier of the gear.
        level: The level of the gear.
    """
    def __init__(
        self,
        name: str,
        id: int,
        level: int
    ):
        """
        Initialize a new GearStat instance.

        Args:
            name: The name of the gear.
            id: The unique identifier of the gear.
            level: The level of the gear.
        """
        self.name = name
        self.id = id
        self.level = level

    def __str__(self) -> str:
        """
        Returns the string representation of the gear stat.

        Returns:
            str: A string containing the gear's name and level.
        """
        return f"{self.name} (Level {self.level})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "GearStat":
        """
        Creates a GearStat instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            GearStat: A new GearStat instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for gear stat data, got {type(json_data)}")

        try:
            return GearStat(
                name=str(json_data.get("name", "")),
                id=int(json_data.get("id", 0)),
                level=int(json_data.get("level", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse gear stat data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing gear stat data: {e}")