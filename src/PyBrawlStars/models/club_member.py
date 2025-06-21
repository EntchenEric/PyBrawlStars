from .player_icon import PlayerIcon
from .club_role import ClubRole
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class ClubMember:
    """
    Represents a member of a club in the game.

    Attributes:
        icon: The player's icon.
        tag: The player's unique tag.
        name: The player's name.
        role: The member's role in the club.
        nameColor: The color of the player's name.
    """
    def __init__(
        self,
        icon: PlayerIcon,
        tag: str,
        name: str,
        role: ClubRole,
        nameColor: str
    ):
        """
        Initialize a new ClubMember instance.

        Args:
            icon: The player's icon.
            tag: The player's unique tag.
            name: The player's name.
            role: The member's role in the club.
            nameColor: The color of the player's name.
        """
        self.icon = icon
        self.tag = tag
        self.name = name
        self.role = role
        self.nameColor = nameColor

    def __str__(self) -> str:
        """
        Returns the string representation of the club member.

        Returns:
            str: The member's name, tag, and role.
        """
        return f"{self.name} ({self.tag}) - {self.role.value}"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "ClubMember":
        """
        Creates a ClubMember instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            ClubMember: A new ClubMember instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for club member data, got {type(json_data)}")

        try:
            icon_data = json_data.get("icon")
            if not isinstance(icon_data, dict):
                raise ParseException(f"Expected 'icon' to be a dictionary, got {type(icon_data)}")
            icon = PlayerIcon.from_json(icon_data, client)

            role_str = json_data.get("role")
            if role_str is None:
                raise ParseException("Missing 'role' field in club member JSON data")
            try:
                role = ClubRole(str(role_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'role': '{role_str}'. Error: {e}")

            return ClubMember(
                icon=icon,
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "N/A")),
                role=role,
                nameColor=str(json_data.get("nameColor", "#ffffff"))
            )
        except (TypeError, ValueError, KeyError) as e:
            raise ParseException(f"Failed to parse club member data: {e}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing club member data: {e}")