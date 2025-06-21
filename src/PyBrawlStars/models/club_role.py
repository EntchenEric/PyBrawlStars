from enum import Enum


class ClubRole(Enum):
    """
    Represents the different roles a player can have in a club.

    Attributes:
        NOT_MEMBER: The player is not a member of the club.
        MEMBER: The player is a regular member of the club.
        PRESIDENT: The player is the president/leader of the club.
        SENIOR: The player is a senior member of the club.
        VICE_PRESIDENT: The player is a vice president of the club.
        UNKNOWN: The player's role is unknown or not set.
    """

    NOT_MEMBER = "notMember"
    """The player is not a member of the club."""

    MEMBER = "member"
    """The player is a regular member of the club."""

    PRESIDENT = "president"
    """The player is the president/leader of the club."""

    SENIOR = "senior"
    """The player is a senior member of the club."""

    VICE_PRESIDENT = "vicePresident"
    """The player is a vice president of the club."""

    UNKNOWN = "unknown"
    """The player's role is unknown or not set."""