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


class ScheduledEvent:
    """
    Represents a scheduled event in the game.

    Attributes:
        start_time: The start time of the event in ISO format.
        end_time: The end time of the event in ISO format.
        mode: The game mode of the event.
        map_name: The name of the map.
        modifiers: List of event modifiers.
        locations: List of event locations.
    """

    start_time: str
    """The start time of the event in ISO format (e.g., '2024-03-20T10:00:00.000Z')."""

    end_time: str
    """The end time of the event in ISO format (e.g., '2024-03-20T18:00:00.000Z')."""

    slot_id: int
    """The ID of the slot of the Event."""

    event_id: int
    """The ID of the Event"""

    mode: GameMode
    """The game mode of the event (e.g., GEM_GRAB, SHOWDOWN)."""

    map_name: str
    """The name of the map where the event takes place."""

    def __init__(
        self,
        start_time: str,
        end_time: str,
        slot_id: int,
        event_id: int,
        mode: GameMode,
        map_name: str,
    ):
        """
        Initialize a new ScheduledEvent instance.

        Args:
            start_time: The start time of the event.
            end_time: The end time of the event.
            mode: The game mode of the event.
            map_name: The name of the map.
            modifiers: List of event modifiers.
            locations: List of event locations.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.slot_id = slot_id
        self.event_id = event_id
        self.mode = mode
        self.map_name = map_name

    def __str__(self) -> str:
        """
        Returns the string representation of the scheduled event.

        Returns:
            str: A string containing the event's mode, map name, and time.
        """
        return f"{self.mode.value} on {self.map_name} ({self.start_time} - {self.end_time})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "ScheduledEvent":
        """
        Creates a ScheduledEvent instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            ScheduledEvent: A new ScheduledEvent instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for scheduled event data, got {type(json_data)}")

        try:
            event_data = json_data.get("event")

            mode_str = event_data.get("mode")
            if mode_str is None:
                raise ParseException("Missing 'mode' field in scheduled event JSON data")
            try:
                mode = GameMode(str(mode_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'mode': '{mode_str}'. Error: {e}")
            return ScheduledEvent(
                start_time=str(json_data.get("startTime", "")),
                end_time=str(json_data.get("endTime", "")),
                slot_id=int(json_data.get("slotId", "0")),
                event_id=int(event_data.get("id", "0")),
                mode=mode,
                map_name=str(event_data.get("map", "")),
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse scheduled event data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing scheduled event data: {e}")