from typing import Any, TYPE_CHECKING, Dict
from .brawler_info import BrawlerInfo

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class PlayerMatchStatus:
    """
    Represents the status of a player in a match.

    Attributes:
        brawler: Information about the player's selected brawler.
        is_ready: Whether the player is ready for the match.
        has_joined: Whether the player has joined the match.
        tag: The player's unique tag.
        ready: Dictionary mapping player tags to their ready status.
        banned: Dictionary mapping player tags to their banned status.
        disconnected: Dictionary mapping player tags to their disconnection status.
    """

    brawler: BrawlerInfo
    """Information about the player's selected brawler."""

    is_ready: bool
    """Whether the player is ready for the match."""

    has_joined: bool
    """Whether the player has joined the match."""

    tag: str
    """The player's unique tag (e.g., '#2qquclvll')."""

    ready: Dict[str, bool]
    """Dictionary mapping player tags to their ready status."""

    banned: Dict[str, bool]
    """Dictionary mapping player tags to their banned status."""

    disconnected: Dict[str, bool]
    """Dictionary mapping player tags to their disconnection status."""

    def __init__(
        self,
        brawler: BrawlerInfo,
        is_ready: bool,
        has_joined: bool,
        tag: str,
        ready: Dict[str, bool],
        banned: Dict[str, bool],
        disconnected: Dict[str, bool]
    ):
        """
        Initialize a new PlayerMatchStatus instance.

        Args:
            brawler: Information about the player's selected brawler.
            is_ready: Whether the player is ready for the match.
            has_joined: Whether the player has joined the match.
            tag: The player's unique tag.
            ready: Dictionary mapping player tags to their ready status.
            banned: Dictionary mapping player tags to their banned status.
            disconnected: Dictionary mapping player tags to their disconnection status.
        """
        self.brawler = brawler
        self.is_ready = is_ready
        self.has_joined = has_joined
        self.tag = tag
        self.ready = ready
        self.banned = banned
        self.disconnected = disconnected

    def __str__(self) -> str:
        """
        Returns the string representation of the player match status.

        Returns:
            str: A string containing the player's tag and status.
        """
        status = []
        if self.has_joined:
            status.append("joined")
        if self.is_ready:
            status.append("ready")
        if self.tag in self.banned and self.banned[self.tag]:
            status.append("banned")
        if self.tag in self.disconnected and self.disconnected[self.tag]:
            status.append("disconnected")
        status_str = ", ".join(status) if status else "no status"
        return f"{self.tag} ({status_str})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "PlayerMatchStatus":
        """
        Creates a PlayerMatchStatus instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            PlayerMatchStatus: A new PlayerMatchStatus instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for player match status data, got {type(json_data)}")

        try:
            brawler_data = json_data.get("brawler")
            if not isinstance(brawler_data, dict):
                raise ParseException(f"Expected 'brawler' to be a dictionary, got {type(brawler_data)}")
            brawler = BrawlerInfo.from_json(brawler_data, client)

            ready_data = json_data.get("ready", {})
            if not isinstance(ready_data, dict):
                raise ParseException(f"Expected 'ready' to be a dictionary, got {type(ready_data)}")
            ready = {str(tag): bool(status) for tag, status in ready_data.items()}

            banned_data = json_data.get("banned", {})
            if not isinstance(banned_data, dict):
                raise ParseException(f"Expected 'banned' to be a dictionary, got {type(banned_data)}")
            banned = {str(tag): bool(status) for tag, status in banned_data.items()}

            disconnected_data = json_data.get("disconnected", {})
            if not isinstance(disconnected_data, dict):
                raise ParseException(f"Expected 'disconnected' to be a dictionary, got {type(disconnected_data)}")
            disconnected = {str(tag): bool(status) for tag, status in disconnected_data.items()}

            return PlayerMatchStatus(
                brawler=brawler,
                is_ready=bool(json_data.get("isReady", False)),
                has_joined=bool(json_data.get("hasJoined", False)),
                tag=str(json_data.get("tag", "")),
                ready=ready,
                banned=banned,
                disconnected=disconnected
            )
        except (TypeError, ValueError) as e:
            raise ParseException(f"Failed to parse player match status data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing player match status data: {e}")