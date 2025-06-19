from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class SiegeStats:
    """
    Represents statistics for a Siege game mode match.

    Attributes:
        bolts_collected: The number of bolts collected.
        siege_damage: The amount of siege damage dealt.
        siege_level: The siege level achieved.
        siege_time: The time spent in siege mode.
    """

    bolts_collected: int
    """The number of bolts collected during the match."""

    siege_damage: int
    """The amount of siege damage dealt to enemy structures."""

    siege_level: int
    """The siege level achieved during the match."""

    siege_time: int
    """The time spent in siege mode, in seconds."""

    def __init__(
        self,
        bolts_collected: int,
        siege_damage: int,
        siege_level: int,
        siege_time: int
    ):
        """
        Initialize a new SiegeStats instance.

        Args:
            bolts_collected: The number of bolts collected.
            siege_damage: The amount of siege damage dealt.
            siege_level: The siege level achieved.
            siege_time: The time spent in siege mode.
        """
        self.bolts_collected = bolts_collected
        self.siege_damage = siege_damage
        self.siege_level = siege_level
        self.siege_time = siege_time

    def __str__(self) -> str:
        """
        Returns the string representation of the siege stats.

        Returns:
            str: A string containing the siege statistics.
        """
        return (f"Level {self.siege_level} siege with {self.bolts_collected} bolts, "
                f"{self.siege_damage} damage in {self.siege_time}s")

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "SiegeStats":
        """
        Creates a SiegeStats instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            SiegeStats: A new SiegeStats instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for siege stats data, got {type(json_data)}")

        try:
            return SiegeStats(
                bolts_collected=int(json_data.get("boltsCollected", 0)),
                siege_damage=int(json_data.get("siegeDamage", 0)),
                siege_level=int(json_data.get("siegeLevel", 0)),
                siege_time=int(json_data.get("siegeTime", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse siege stats data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing siege stats data: {e}")