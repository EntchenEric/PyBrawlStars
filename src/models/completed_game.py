from models.completed_game_team import CompletedGameTeam
from models.termination_reason import TerminationReason
from typing import Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class CompletedGame:
    """
    Represents a completed game.

    Attributes:
        teams: List of teams that participated in the game.
        termination_reason: The reason why the game ended.
        duration: The duration of the game in seconds.
        winning_side: The side number of the winning team.
    """

    teams: List[CompletedGameTeam]
    """List of teams that participated in the game, containing their final stats and results."""

    termination_reason: TerminationReason
    """The reason why the game ended (e.g., NORMAL, DISCONNECT, SURRENDER)."""

    duration: int
    """The duration of the game in seconds."""

    winning_side: int
    """The side number (0 or 1) of the winning team. In solo modes, represents the winning player's side."""

    def __init__(
        self,
        teams: List[CompletedGameTeam],
        termination_reason: TerminationReason,
        duration: int,
        winning_side: int
    ):
        """
        Initialize a new CompletedGame instance.

        Args:
            teams: List of teams that participated in the game.
            termination_reason: The reason why the game ended.
            duration: The duration of the game in seconds.
            winning_side: The side number of the winning team.
        """
        self.teams = teams
        self.termination_reason = termination_reason
        self.duration = duration
        self.winning_side = winning_side

    def __str__(self) -> str:
        """
        Returns the string representation of the completed game.

        Returns:
            str: A string containing the game duration and winning team.
        """
        return f"Game completed in {self.duration}s (Winner: Team {self.winning_side})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "CompletedGame":
        """
        Creates a CompletedGame instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            CompletedGame: A new CompletedGame instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for completed game data, got {type(json_data)}")

        try:
            teams_data = json_data.get("teams", [])
            if not isinstance(teams_data, list):
                raise ParseException(f"Expected 'teams' to be a list, got {type(teams_data)}")
            teams = [CompletedGameTeam.from_json(t, client) for t in teams_data if isinstance(t, dict)]

            termination_reason_str = json_data.get("terminationReason")
            if termination_reason_str is None:
                raise ParseException("Missing 'terminationReason' field in completed game JSON data")
            try:
                termination_reason = TerminationReason(str(termination_reason_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'terminationReason': '{termination_reason_str}'. Error: {e}")

            return CompletedGame(
                teams=teams,
                termination_reason=termination_reason,
                duration=int(json_data.get("duration", 0)),
                winning_side=int(json_data.get("winningSide", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse completed game data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing completed game data: {e}")