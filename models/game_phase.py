from enum import Enum


class GamePhase(Enum):
    """
    Represents the different phases of a game.

    Attributes:
        NOT_STARTED: The game has not started yet.
        PREPARATION: Players are preparing for the game (e.g., selecting brawlers).
        IN_PROGRESS: The game is currently being played.
        ENDED: The game has ended.
        CANCELLED: The game was cancelled before completion.
        DRAFT: Players are in the draft phase (for competitive matches).
        MATCHMAKING: The game is in the matchmaking phase.
        LOADING: The game is loading.
        RESULT: The game is showing the results screen.
    """

    NOT_STARTED = "NOT_STARTED"
    """The game has not started yet."""

    PREPARATION = "PREPARATION"
    """Players are preparing for the game (e.g., selecting brawlers)."""

    IN_PROGRESS = "IN_PROGRESS"
    """The game is currently being played."""

    ENDED = "ENDED"
    """The game has ended."""

    CANCELLED = "CANCELLED"
    """The game was cancelled before completion."""

    DRAFT = "DRAFT"
    """Players are in the draft phase (for competitive matches)."""

    MATCHMAKING = "MATCHMAKING"
    """The game is in the matchmaking phase."""

    LOADING = "LOADING"
    """The game is loading."""

    RESULT = "RESULT"
    INIT = "init"
    BAN_HEROES = "banHeroes"
    PICK_HEROES = "pickHeroes"
    FINAL_PREPERATION = "finalPreperation"
    BATTLE = "battle"
    MATCH_RESULT = "matchResult"
    ENDING = "ending"