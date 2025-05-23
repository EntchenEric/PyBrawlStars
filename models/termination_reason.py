from enum import Enum

class TerminationReason(Enum):
    NONE = "none"
    PLAYER_DISCONNECTED = "playerDisconnected"
    PLAYER_NOT_RESPONDING = "playerNotResponding"
    TECHNICAL_ERROR  = "technicalError"
    MATCH_TOO_LONG = "matchTooLong"
    OTHER = "other"