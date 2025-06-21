from enum import Enum


class ClubType(Enum):
    """
    Represents the different types of clubs.

    Attributes:
        OPEN: Anyone can join the club without an invitation.
        INVITE_ONLY: Players need an invitation to join the club.
        CLOSED: The club is closed and not accepting new members.
        UNKNOWN: The club type is unknown or not set.
    """

    OPEN = "open"
    """Anyone can join the club without an invitation."""

    INVITE_ONLY = "inviteOnly"
    """Players need an invitation to join the club."""

    CLOSED = "closed"
    """The club is closed and not accepting new members."""

    UNKNOWN = "unknown"
    """The club type is unknown or not set."""