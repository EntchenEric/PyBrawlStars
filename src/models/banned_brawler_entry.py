from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class BannedBrawlerEntry:
    """
    Represents a banned brawler entry in a match.

    Attributes:
        brawler_id: The unique identifier of the banned brawler.
        team_index: The index of the team that banned the brawler.
        pick_order: The order in which the brawler was banned.
    """

    brawler_id: int
    """The unique identifier of the banned brawler."""

    team_index: int
    """The index of the team that banned the brawler (0 or 1)."""

    pick_order: int
    """The order in which the brawler was banned (starting from 0)."""

    def __init__(
        self,
        brawler_id: int,
        team_index: int,
        pick_order: int
    ):
        """
        Initialize a new BannedBrawlerEntry instance.

        Args:
            brawler_id: The unique identifier of the banned brawler.
            team_index: The index of the team that banned the brawler.
            pick_order: The order in which the brawler was banned.
        """
        self.brawler_id = brawler_id
        self.team_index = team_index
        self.pick_order = pick_order

    def __str__(self) -> str:
        """
        Returns the string representation of the banned brawler entry.

        Returns:
            str: A string containing the brawler ID and team info.
        """
        return f"Brawler {self.brawler_id} banned by Team {self.team_index} (Pick {self.pick_order + 1})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "BannedBrawlerEntry":
        """
        Creates a BannedBrawlerEntry instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            BannedBrawlerEntry: A new BannedBrawlerEntry instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for banned brawler entry data, got {type(json_data)}")

        try:
            return BannedBrawlerEntry(
                brawler_id=int(json_data.get("brawlerId", 0)),
                team_index=int(json_data.get("teamIndex", 0)),
                pick_order=int(json_data.get("pickOrder", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse banned brawler entry data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing banned brawler entry data: {e}")