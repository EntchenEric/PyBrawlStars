from enum import Enum


class TerminationReason(Enum):
    """
    Represents the reason why a match was terminated.

    Attributes:
        NORMAL: The match ended normally.
        DISCONNECT: A player disconnected from the match.
        TIMEOUT: The match timed out.
        SURRENDER: A team surrendered the match.
        DRAW: The match ended in a draw.
        CANCELLED: The match was cancelled.
        ERROR: The match encountered an error.
        ABANDONED: The match was abandoned by players.
        INACTIVITY: Players were inactive for too long.
        MAINTENANCE: Server maintenance interrupted the match.
        INVALID_STATE: The match entered an invalid state.
        CHEATING: Cheating was detected in the match.
        SERVER_ERROR: A server error occurred.
        CLIENT_ERROR: A client error occurred.
        NETWORK_ERROR: A network error occurred.
    """

    NORMAL = "NORMAL"
    """The match ended normally."""

    DISCONNECT = "DISCONNECT"
    """A player disconnected from the match."""

    TIMEOUT = "TIMEOUT"
    """The match timed out."""

    SURRENDER = "SURRENDER"
    """A team surrendered the match."""

    DRAW = "DRAW"
    """The match ended in a draw."""

    CANCELLED = "CANCELLED"
    """The match was cancelled."""

    ERROR = "ERROR"
    """The match encountered an error."""

    ABANDONED = "ABANDONED"
    """The match was abandoned by players."""

    INACTIVITY = "INACTIVITY"
    """Players were inactive for too long."""

    MAINTENANCE = "MAINTENANCE"
    """Server maintenance interrupted the match."""

    INVALID_STATE = "INVALID_STATE"
    """The match entered an invalid state."""

    CHEATING = "CHEATING"
    """Cheating was detected in the match."""

    SERVER_ERROR = "SERVER_ERROR"
    """A server error occurred."""

    CLIENT_ERROR = "CLIENT_ERROR"
    """A client error occurred."""

    NETWORK_ERROR = "NETWORK_ERROR"
    """A network error occurred."""