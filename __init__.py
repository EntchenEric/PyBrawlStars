"""
PyBrawlStars - An asynchronous Python API wrapper for the Brawl Stars API

A modern, async-first Python library for interacting with the Brawl Stars API.
Provides easy access to player statistics, club information, battle logs, and more.
"""

from .client import BSClient
from .models.errors.api_error import APIError  
from .models.errors.network_error import NetworkError
from .models.errors.client_error import ClientError

__version__ = "1.0.0"
__author__ = "EntchenEric"
__license__ = "MIT"

__all__ = [
    "BSClient",
    "APIError",
    "NetworkError", 
    "ClientError"
] 