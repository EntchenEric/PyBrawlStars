from .match_team_player import MatchTeamPlayer
from .brawler_info import BrawlerInfo
from typing import Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class MatchTeam:
    """
    Represents a team in a match.

    Attributes:
        players: List of players in the team.
        bans: List of banned brawlers.
        side: The team's side number.
    """

    players: List[MatchTeamPlayer]
    """List of players in the team, containing their information and match-specific details."""

    bans: List[BrawlerInfo]
    """List of brawlers that are banned for this team in the match (e.g., in Power League)."""

    side: int
    """The team's side number (0 or 1) indicating which side of the map they start on."""

    def __init__(
        self,
        players: List[MatchTeamPlayer],
        bans: List[BrawlerInfo],
        side: int
    ):
        """
        Initialize a new MatchTeam instance.

        Args:
            players: List of players in the team.
            bans: List of banned brawlers.
            side: The team's side number.
        """
        self.players = players
        self.bans = bans
        self.side = side

    def __str__(self) -> str:
        """
        Returns the string representation of the match team.

        Returns:
            str: A string containing the team's side and number of players.
        """
        return f"Team {self.side} ({len(self.players)} players)"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "MatchTeam":
        """
        Creates a MatchTeam instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            MatchTeam: A new MatchTeam instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for match team data, got {type(json_data)}")

        try:
            players_data = json_data.get("players", [])
            if not isinstance(players_data, list):
                raise ParseException(f"Expected 'players' to be a list, got {type(players_data)}")
            players = [MatchTeamPlayer.from_json(p, client) for p in players_data if isinstance(p, dict)]

            bans_data = json_data.get("bans", [])
            if not isinstance(bans_data, list):
                raise ParseException(f"Expected 'bans' to be a list, got {type(bans_data)}")
            bans = [BrawlerInfo.from_json(b, client) for b in bans_data if isinstance(b, dict)]

            return MatchTeam(
                players=players,
                bans=bans,
                side=int(json_data.get("side", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse match team data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing match team data: {e}")