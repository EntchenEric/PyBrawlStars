from enum import Enum


class MatchState(Enum):
    """
    Represents the different states of a match.

    Attributes:
        WAITING: The match is waiting for players to join.
        READY: All players have joined and are ready.
        IN_PROGRESS: The match is currently being played.
        ENDED: The match has ended normally.
        CANCELLED: The match was cancelled before completion.
        ERROR: The match encountered an error.
        ABANDONED: The match was abandoned by players.
        TIMEOUT: The match timed out.
        DRAFT: The match is in the draft phase.
        MATCHMAKING: The match is in the matchmaking phase.
        LOADING: The match is loading.
        RESULT: The match is showing the results screen.
    """

    WAITING = "WAITING"
    """The match is waiting for players to join."""

    READY = "READY"
    """All players have joined and are ready."""

    IN_PROGRESS = "IN_PROGRESS"
    """The match is currently being played."""

    ENDED = "ENDED"
    """The match has ended normally."""

    CANCELLED = "CANCELLED"
    """The match was cancelled before completion."""

    ERROR = "ERROR"
    """The match encountered an error."""

    ABANDONED = "ABANDONED"
    """The match was abandoned by players."""

    TIMEOUT = "TIMEOUT"
    """The match timed out."""

    DRAFT = "DRAFT"
    """The match is in the draft phase."""

    MATCHMAKING = "MATCHMAKING"
    """The match is in the matchmaking phase."""

    LOADING = "LOADING"
    """The match is loading."""

    RESULT = "RESULT"
    """The match is showing the results screen."""