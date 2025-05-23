from enum import Enum

class ClubRole(Enum):
    NOT_MEMBER = "notMember"
    MEMBER = "member"
    PRESIDENT = "president"
    SENIOR = "senior"
    VICE_PRESIDENT = "vicePresident"
    UNKNOWN = "unknown"