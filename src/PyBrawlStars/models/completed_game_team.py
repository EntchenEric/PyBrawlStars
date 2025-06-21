from .siege_stats import SiegeStats
from .player_entry_completed_game import PlayerEntryCompletedGame
from typing import Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class CompletedGameTeam:
    """
    Represents a team in a completed game.

    Attributes:
        players: List of players who participated in the game.
        side: The side number of the team.
    """

    players: List[PlayerEntryCompletedGame]
    """List of players who participated in the game, containing their final stats and performance."""

    side: int
    """The side number (0 or 1) indicating which side of the map the team started on."""

    def __init__(
        self,
        players: List[PlayerEntryCompletedGame],
        side: int
    ):
        """
        Initialize a new CompletedGameTeam instance.

        Args:
            players: List of players who participated in the game.
            side: The side number of the team.
        """
        self.players = players
        self.side = side

    def __str__(self) -> str:
        """
        Returns the string representation of the completed game team.

        Returns:
            str: A string containing the team's side and number of players.
        """
        return f"Team {self.side} ({len(self.players)} players)"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "CompletedGameTeam":
        """
        Creates a CompletedGameTeam instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            CompletedGameTeam: A new CompletedGameTeam instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for completed game team data, got {type(json_data)}")

        try:
            players_data = json_data.get("players", [])
            if not isinstance(players_data, list):
                raise ParseException(f"Expected 'players' to be a list, got {type(players_data)}")
            players = [PlayerEntryCompletedGame.from_json(p, client) for p in players_data if isinstance(p, dict)]

            return CompletedGameTeam(
                players=players,
                side=int(json_data.get("side", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse completed game team data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing completed game team data: {e}")