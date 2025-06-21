from .club_type import ClubType
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class ClubRanking:
    """
    Represents a club's ranking information.

    Attributes:
        tag: The club's unique tag.
        name: The name of the club.
        rank: The club's current rank.
        trophies: The club's total trophies.
        member_count: The number of members in the club.
        club_type: The type of the club.
        required_trophies: The minimum trophies required to join.
    """

    tag: str
    """The club's unique tag (e.g., '#2JU2GR0')."""

    name: str
    """The name of the club."""

    rank: int
    """The club's current rank in the leaderboard."""

    trophies: int
    """The total number of trophies the club has."""

    member_count: int
    """The current number of members in the club."""

    club_type: ClubType
    """The type of the club (e.g., open, invite only, closed)."""

    required_trophies: int
    """The minimum number of trophies required to join the club."""

    def __init__(
        self,
        tag: str,
        name: str,
        rank: int,
        trophies: int,
        member_count: int,
        club_type: ClubType,
        required_trophies: int
    ):
        """
        Initialize a new ClubRanking instance.

        Args:
            tag: The club's unique tag.
            name: The name of the club.
            rank: The club's current rank.
            trophies: The club's total trophies.
            member_count: The number of members in the club.
            club_type: The type of the club.
            required_trophies: The minimum trophies required to join.
        """
        self.tag = tag
        self.name = name
        self.rank = rank
        self.trophies = trophies
        self.member_count = member_count
        self.club_type = club_type
        self.required_trophies = required_trophies

    def __str__(self) -> str:
        """
        Returns the string representation of the club ranking.

        Returns:
            str: A string containing the club's rank, name, and trophy count.
        """
        return f"#{self.rank} {self.name} ({self.trophies} trophies)"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "ClubRanking":
        """
        Creates a ClubRanking instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            ClubRanking: A new ClubRanking instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for club ranking data, got {type(json_data)}")

        try:
            club_type_str = json_data.get("type")
            if club_type_str is None:
                raise ParseException("Missing 'type' field in club ranking JSON data")
            try:
                club_type = ClubType(str(club_type_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'type': '{club_type_str}'. Error: {e}")

            return ClubRanking(
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "")),
                rank=int(json_data.get("rank", 0)),
                trophies=int(json_data.get("trophies", 0)),
                member_count=int(json_data.get("memberCount", 0)),
                club_type=club_type,
                required_trophies=int(json_data.get("requiredTrophies", 0))
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse club ranking data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing club ranking data: {e}")