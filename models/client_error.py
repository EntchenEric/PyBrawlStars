from models.parse_error import ParseException

class ClientError:
    reason: str
    message: str
    type: str | None
    detail: dict[str, str] | None

    def __init__(self, reason: str, message: str, type: str | None = None, detail: dict[str, str] | None = None):
        self.reason = reason
        self.message = message
        self.type = type
        self.detail = detail

    def __str__(self):
        return f"Client Error: {self.type} | {self.reason}\n{self.message}\n{self.detail}"

def from_json(json: dict[str, str | dict[str, str]]) -> ClientError:
    try:
        return ClientError(reason = json.get("reason", ""), message = json.get("message", ""), type = json.get(type, ""), detail = json.get("detail", {}))
    except:
        raise ParseException()