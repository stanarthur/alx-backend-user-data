#!/usr/bin/env python3
"""Authentication module for the API.
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of strings excluded_paths.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths to be excluded.

        Returns:
            bool: True if path should be authenticated, False otherwise.
        """
        if path is None or not excluded_paths:
            return True

        path = path.rstrip("/")  # Remove trailing slashes from path
        excluded_paths = [p.rstrip("/") for p in excluded_paths]

        for excluded_path in excluded_paths:
            if '*' in excluded_path:
                prefix = excluded_path.rstrip('*')
                if path.startswith(prefix):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        If request is None, returns an empty string.
        If request doesn’t contain the header key Authorization,
        returns an empty string.
        Otherwise, return the value of the header request Authorization.
        """
        if request is None or 'Authorization' not in request.headers:
            return ''
        return request.headers.get('Authorization', '')

    def current_user(self, request=None):
        """It returns None
        """
        return None

    def session_cookie(self, request=None) -> str:
        """Returns a cookie value from a request
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME', "_my_session_id")
        return request.cookies.get(session_name)
