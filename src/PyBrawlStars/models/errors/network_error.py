from .client_error import ClientError

class NetworkError(ClientError):
    """Raised for network-related issues (e.g., connection refused)."""
    pass