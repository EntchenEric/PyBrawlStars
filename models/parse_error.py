class ParseException(Exception):
    def __init__(self, message: str = "Failed to parse Response to Json. This may be a issue from the wrapper. Consider reporting this."):
        super().__init__(message)