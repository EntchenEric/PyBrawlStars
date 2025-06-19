from enum import Enum


class MatchMode(Enum):
    """
    Represents the different modes of a match.

    Attributes:
        NORMAL: A standard match without special rules.
        FRIENDLY: A friendly match between players.
        RANKED: A ranked match that affects player rankings.
        POWER_LEAGUE: A match in the Power League competitive mode.
        CHALLENGE: A match in a challenge event.
        CHAMPIONSHIP: A match in the championship challenge.
        CLUB_LEAGUE: A match in the Club League mode.
        TEAM_LEAGUE: A match in the Team League mode.
        TRAINING: A training match against bots.
        CUSTOM: A custom match with custom rules.
    """

    NORMAL = "NORMAL"
    """A standard match without special rules."""

    FRIENDLY = "FRIENDLY"
    """A friendly match between players."""

    RANKED = "RANKED"
    """A ranked match that affects player rankings."""

    POWER_LEAGUE = "POWER_LEAGUE"
    """A match in the Power League competitive mode."""

    CHALLENGE = "CHALLENGE"
    """A match in a challenge event."""

    CHAMPIONSHIP = "CHAMPIONSHIP"
    """A match in the championship challenge."""

    CLUB_LEAGUE = "CLUB_LEAGUE"
    """A match in the Club League mode."""

    TEAM_LEAGUE = "TEAM_LEAGUE"
    """A match in the Team League mode."""

    TRAINING = "TRAINING"
    """A training match against bots."""

    CUSTOM = "CUSTOM"
    """A custom match with custom rules."""