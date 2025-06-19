from models.battle_result import BattleResult
from models.event import Event
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Battle:
    """
    Represents a battle in the game.

    Attributes:
        battle: The battle result information.
        battle_time: The timestamp of when the battle occurred.
        event: The event information for this battle.
    """

    battle_result: BattleResult
    """The battle result information, containing details about the outcome, teams, and statistics."""

    battle_time: str
    """The timestamp of when the battle occurred in ISO 8601 format (e.g., '20240315T123456.000Z')."""

    event: Event
    """The event information for this battle, including game mode, map, and modifiers."""

    def __init__(
        self,
        battle_result: BattleResult,
        battle_time: str,
        event: Event
    ):
        """
        Initialize a new Battle instance.

        Args:
            battle: The battle result information.
            battle_time: The timestamp of when the battle occurred.
            event: The event information for this battle.
        """
        self.battle_result = battle_result
        self.battle_time = battle_time
        self.event = event

    def __str__(self) -> str:
        """
        Returns the string representation of the battle.

        Returns:
            str: A string containing the battle time and event information.
        """
        return f"Battle at {self.battle_time} - {self.event}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Battle":
        """
        Creates a Battle instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Battle: A new Battle instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for battle data, got {type(json_data)}")

        try:
            battle_data = json_data.get("battle")
            if not isinstance(battle_data, dict):
                raise ParseException(f"Expected 'battle' to be a dictionary, got {type(battle_data)}")
            battle_result = BattleResult.from_json(battle_data, client)

            event_data = json_data.get("event")
            if not isinstance(event_data, dict):
                raise ParseException(f"Expected 'event' to be a dictionary, got {type(event_data)}")
            event = Event.from_json(event_data, client)

            return Battle(
                battle_result=battle_result,
                battle_time=str(json_data.get("battleTime", "")),
                event=event
            )
        except (TypeError, ValueError, KeyError) as e:
            raise ParseException(f"Failed to parse battle data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing battle data: {e}")