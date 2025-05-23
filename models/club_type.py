from enum import Enum

class ClubType(Enum):
    OPEN = "open"
    INVITE_ONLY = "inviteOnly"
    CLOSED = "closed"
    UNKNOWN = "unknown"