from models.parse_error import ParseException

class GearStat:
    name: str
    id: int
    level: int

def from_json(json: dict[str, str]):
    try:
        return GearStat(
            name = json.get("name"), 
                        id = int(json.get("id")), 
                        level = int(json.get("level"))
                    )
    except:
        raise ParseException()