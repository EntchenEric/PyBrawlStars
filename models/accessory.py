from models.parse_error import ParseException

class Accessory:
    name: str
    id: int

def from_json(json: dict[str, str]) -> Accessory:
    try:
        return Accessory(name = json.get("name"), id = int(json.get("id")))
    except:
        raise ParseException()