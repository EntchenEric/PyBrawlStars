class ParseException(Exception):
    """
    Exception raised when parsing JSON data fails in the Brawl Stars API wrapper.

    This may indicate a problem with the API response or a bug in the wrapper. Consider reporting this if it persists.
    """
    def __init__(self, message: str = "Failed to parse Response to Json. This may be a issue from the wrapper. Consider reporting this."):
        super().__init__(message)