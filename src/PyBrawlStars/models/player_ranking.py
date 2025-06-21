from .player_icon import PlayerIcon
from .player_club import PlayerClub
from typing import Any, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class PlayerRanking:
    """
    Represents a player's ranking information.

    Attributes:
        club: The player's club information.
        icon: The player's icon.
        tag: The player's unique tag.
        name: The player's name.
        name_color: The color of the player's name.
        rank: The player's current rank.
        trophies: The player's total trophies.
    """

    club: Optional[PlayerClub]
    """The club the player is currently in, or None if not in a club."""

    icon: PlayerIcon
    """The player's selected icon object, containing icon ID and other details."""

    tag: str
    """The unique player tag (e.g., '#2qquclvll')."""

    name: str
    """The player's current in-game name."""

    name_color: str
    """The hexadecimal color code for the player's name (e.g., '0xffc03aff')."""

    rank: int
    """The player's current rank in the leaderboard."""

    trophies: int
    """The current number of trophies the player has."""

    def __init__(
        self,
        club: Optional[PlayerClub],
        icon: PlayerIcon,
        tag: str,
        name: str,
        name_color: str,
        rank: int,
        trophies: int
    ):
        """
        Initialize a new PlayerRanking instance.

        Args:
            club: The player's club information.
            icon: The player's icon.
            tag: The player's unique tag.
            name: The player's name.
            name_color: The color of the player's name.
            rank: The player's current rank.
            trophies: The player's total trophies.
        """
        self.club = club
        self.icon = icon
        self.tag = tag
        self.name = name
        self.name_color = name_color
        self.rank = rank
        self.trophies = trophies

    def __str__(self) -> str:
        """
        Returns the string representation of the player ranking.

        Returns:
            str: A string containing the player's rank, name, and trophy count.
        """
        club_str = f" [{self.club.name}]" if self.club else ""
        return f"#{self.rank} {self.name}{club_str} ({self.trophies} trophies)"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerRanking":
        """
        Creates a PlayerRanking instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerRanking: A new PlayerRanking instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player ranking data, got {type(json_data)}")

        try:
            club_data = json_data.get("club")
            club = PlayerClub.from_json(club_data, client) if isinstance(club_data, dict) else None

            icon_data = json_data.get("icon")
            if not isinstance(icon_data, dict):
                raise ParseException(f"Expected 'icon' to be a dictionary, got {type(icon_data)}")
            icon = PlayerClub.from_json(icon_data, client)

            return PlayerRanking(
                club=club,
                icon=icon,
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "")),
                name_color=str(json_data.get("nameColor", "0x00000000")),
                rank=int(json_data.get("rank", 0)),
                trophies=int(json_data.get("trophies", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player ranking data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player ranking data: {e}")