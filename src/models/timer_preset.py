from enum import Enum


class TimerPreset(Enum):
    """
    Represents preset timer configurations for matches.

    Attributes:
        NORMAL: Standard match timer settings.
        EXTENDED: Extended match timer settings.
        SHORT: Shortened match timer settings.
        QUICK: Quick match timer settings.
        TOURNAMENT: Tournament match timer settings.
        PRACTICE: Practice match timer settings.
        CUSTOM: Custom timer settings.
        INFINITE: No time limit.
    """

    NORMAL = "NORMAL"
    """Standard match timer settings (e.g., 3 minutes for Gem Grab)."""

    EXTENDED = "EXTENDED"
    """Extended match timer settings (e.g., 5 minutes for longer matches)."""

    SHORT = "SHORT"
    """Shortened match timer settings (e.g., 2 minutes for quick games)."""

    QUICK = "QUICK"
    """Quick match timer settings (e.g., 1 minute for very fast games)."""

    TOURNAMENT = "TOURNAMENT"
    """Tournament match timer settings (e.g., standardized timers for competitive play)."""

    PRACTICE = "PRACTICE"
    """Practice match timer settings (e.g., longer timers for training)."""

    CUSTOM = "CUSTOM"
    """Custom timer settings (user-defined)."""

    INFINITE = "INFINITE"
    """No time limit (e.g., for training or special modes)."""