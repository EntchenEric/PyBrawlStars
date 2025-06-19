from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class BattleRegion:
    """
    Represents a battle region in the game.

    Attributes:
        id: The unique identifier of the region.
        name: The name of the region.
    """

    id: int
    """The unique identifier of the region."""

    name: str
    """The name of the region (e.g., 'Europe', 'North America')."""

    def __init__(
        self,
        id: int,
        name: str
    ):
        """
        Initialize a new BattleRegion instance.

        Args:
            id: The unique identifier of the region.
            name: The name of the region.
        """
        self.id = id
        self.name = name

    def __str__(self) -> str:
        """
        Returns the string representation of the battle region.

        Returns:
            str: The region's name.
        """
        return self.name

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BattleRegion":
        """
        Creates a BattleRegion instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BattleRegion: A new BattleRegion instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for battle region data, got {type(json_data)}")

        try:
            return BattleRegion(
                id=int(json_data.get("id", 0)),
                name=str(json_data.get("name", ""))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse battle region data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing battle region data: {e}")