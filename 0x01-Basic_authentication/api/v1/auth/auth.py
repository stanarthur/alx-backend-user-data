#!/usr/bin/env python3
"""Authentication module for the API.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """It checks if a path requires authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """It returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """It returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """It returns None
        """
        return None
