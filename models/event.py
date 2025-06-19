from models.game_mode import GameMode
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Event:
    """
    Represents an event in the game.

    Attributes:
        mode: The game mode of the event.
        id: The unique identifier of the event.
        map: The map name for the event.
    """

    mode: GameMode
    """The game mode of the event (e.g., GEM_GRAB, SHOWDOWN, BRAWL_BALL)."""

    id: int
    """The unique identifier of the event in the game."""

    map: str
    """The name of the map where the event takes place (e.g., 'Snake Prairie', 'Hard Rock Mine')."""

    def __init__(
        self,
        mode: GameMode,
        id: int,
        map: str
    ):
        """
        Initialize a new Event instance.

        Args:
            mode: The game mode of the event.
            id: The unique identifier of the event.
            map: The map name for the event.
        """
        self.mode = mode
        self.id = id
        self.map = map

    def __str__(self) -> str:
        """
        Returns the string representation of the event.

        Returns:
            str: A string containing the event mode and map name.
        """
        return f"{self.mode.value} on {self.map}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Event":
        """
        Creates an Event instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Event: A new Event instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for event data, got {type(json_data)}")

        try:
            mode_str = json_data.get("mode")
            if mode_str is None:
                raise ParseException("Missing 'mode' field in event JSON data")
            try:
                mode = GameMode(str(mode_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'mode': '{mode_str}'. Error: {e}")

            return Event(
                mode=mode,
                id=int(json_data.get("id", 0)),
                map=str(json_data.get("map", "Unknown Map"))
            )
        except (TypeError, ValueError, KeyError) as e:
            raise ParseException(f"Failed to parse event data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing event data: {e}")