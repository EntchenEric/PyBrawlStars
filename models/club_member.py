from models.player_icon import PlayerIcon
from models.club_role import ClubRole

class ClubMember:
    icon: PlayerIcon
    tag: str
    name: str
    role: ClubRole
    nameColor: str