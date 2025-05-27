from models.club_member import ClubMember
from models.club_type import ClubType
from client import BSClient
from typing import Any

class Club:
    client: BSClient
    tag: str
    name: str
    description: str
    trophies: int
    required_trophies: int
    members: list[ClubMember]
    type: ClubType
    badge_id: int

    def __init__(
        self,
        client: BSClient,
        tag: str,
        name: str,
        description: str,
        trophies: int,
        required_trophies: int,
        members: list[ClubMember],
        type: ClubType,
        badge_id: int,
    ):
        self.client = client
        self.tag = tag
        self.name = name
        self.description = description
        self.trophies = trophies
        self.required_trophies = required_trophies
        self.members = members
        self.type = type
        self.badge_id = badge_id

def from_json(json_data: dict[str, Any], client: BSClient):
    ...