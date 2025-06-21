from .club_member import ClubMember
from .club_type import ClubType
from typing import Any, TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from client import BSClient

try:
    from models.parse_error import ParseException
except ImportError:
    class ParseException(Exception):
        """Custom exception for parsing errors."""
        pass


class Club:
    """
    Represents a Club in the game.

    Attributes:
        client: An instance of BSClient for potential API interactions.
        tag: The unique club tag (e.g., '#2JU2GR0').
        name: The name of the club.
        description: The club's description.
        trophies: The total number of trophies of the club (sum of member trophies).
        required_trophies: The minimum number of trophies required to join the club.
        members: A list of `ClubMember` objects representing the members of the club.
        type: The type of the club (e.g., open, invite only, closed), represented by `ClubType`.
        badge_id: The ID of the club's badge.
    """
    def __init__(
        self,
        client: "BSClient",
        tag: str,
        name: str,
        description: str,
        trophies: int,
        required_trophies: int,
        members: List[ClubMember],
        type: ClubType,
        badge_id: int,
    ):
        """
        Initializes a new Club instance.

        Args:
            client: The BSClient instance.
            tag: The club's unique tag.
            name: The club's name.
            description: The club's description.
            trophies: Total club trophies.
            required_trophies: Trophies required to join.
            members: List of club members.
            type: The club's type (e.g., an instance of the ClubType enum).
            badge_id: The club's badge ID.
        """
        self.client = client
        self.tag = tag
        self.name = name
        self.description = description
        self.trophies = trophies
        self.required_trophies = required_trophies
        self.members = members
        self.type = type
        self.badge_id = badge_id

    def __str__(self) -> str:
        """
        Returns the string representation of the club.

        Returns:
            str: The club's name and tag.
        """
        return f"{self.name} ({self.tag})"

    @staticmethod
    def from_json(json_data: dict[str, Any], client: "BSClient") -> "Club":
        """
        Creates a Club instance from JSON data.

        Args:
            json_data (dict[str, Any]): The JSON data to parse.
            client (BSClient): The BSClient instance.

        Returns:
            Club: A new Club instance.

        Raises:
            ParseException: If the JSON data is invalid or missing required fields.
        """
        if not isinstance(json_data, dict):
            raise ParseException(f"Expected a dictionary for club data, got {type(json_data)}")

        try:
            members_data = json_data.get("members", [])
            parsed_members: List[ClubMember] = []
            if isinstance(members_data, list):
                for member_item_data in members_data:
                    if isinstance(member_item_data, dict):
                        parsed_members.append(ClubMember.from_json(member_item_data, client))
                    else:
                        print(f"Warning: Skipping non-dictionary item in 'members' list: {member_item_data}")
            elif members_data is not None:
                raise ParseException(f"Expected 'members' to be a list, got {type(members_data)}.")

            club_type_str = json_data.get("type")
            if club_type_str is None:
                raise ParseException("Missing 'type' field in club JSON data.")
            try:
                parsed_club_type = ClubType(str(club_type_str))
            except ValueError as e:
                raise ParseException(f"Invalid value for 'type': '{club_type_str}'. Error: {e}")

            return Club(
                client=client,
                tag=str(json_data.get("tag", "")),
                name=str(json_data.get("name", "N/A")),
                description=str(json_data.get("description", "")),
                trophies=int(json_data.get("trophies", 0)),
                required_trophies=int(json_data.get("requiredTrophies", 0)),
                members=parsed_members,
                type=parsed_club_type,
                badge_id=int(json_data.get("badgeId", 0))
            )
        except (TypeError, ValueError, KeyError) as e:
            raise ParseException(f"Failed to parse club data due to type, value, or key error: {e}. "
                             f"Input snippet (first 200 chars): {str(json_data)[:200]}")
        except Exception as e:
            raise ParseException(f"An unexpected error occurred while parsing club data: {e}")