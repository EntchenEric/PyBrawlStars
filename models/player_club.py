from models.parse_error import ParseException

class PlayerClub:
    name: str
    tag: str

    def __init__(self, name: str, tag: str):
        self.name = name
        self.tag = tag

def from_json(json: dict[str, str]) -> PlayerClub:
    try:
        print("json: ", json)
        PlayerClub(name = json.get("name"), tag = json.get("tag"))
    except:
        raise ParseException()