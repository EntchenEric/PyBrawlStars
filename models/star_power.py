from models.parse_error import ParseException

class StarPower:
    name: str
    id: int

def from_json(json: dict[str, str]) -> StarPower:
    try:
        return StarPower(name = json.get("name"), id = int(json.get("id")))
    except:
        raise ParseException()