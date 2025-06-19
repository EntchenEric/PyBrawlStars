from models.errors.client_error import ClientError

class APIError(ClientError):
    """Raised for non-2xx API responses."""
    def __init__(self, status_code: int, error_json: dict | None = None):
        self.status_code = status_code
        self.error_json = error_json
        self.reason = error_json.get('reason') if error_json else "Unknown"
        self.message = error_json.get('message') if error_json else f"API returned status {status_code}"
        super().__init__(reason=self.reason, message=self.message)