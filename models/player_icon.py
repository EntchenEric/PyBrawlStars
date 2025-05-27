from models.parse_error import ParseException

class PlayerIcon:
    id: int

    def __init__(self, id: int):
        self.id = id

def from_json(json: dict[str, str]) -> PlayerIcon:
    try:
        return PlayerIcon(id = int(json.get("id")))
    except:
        raise ParseException()