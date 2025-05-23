from models.club_member import ClubMember
from models.club_type import ClubType

class Club:
    tag: str
    name: str
    description: str
    trophies: int
    required_trophies: int
    members: list[ClubMember]
    type: ClubType
    badge_id: int