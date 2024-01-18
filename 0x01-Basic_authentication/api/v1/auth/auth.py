#!/usr/bin/env python3
"""Authentication module for the API.
"""
from flask import request
from typing import List, TypeVar


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
        if path is None:
            """Returns True if path is None
            """
            return True

        if not excluded_paths:
            """Returns True if excluded_paths is empty
            """
            return True

        path = path.rstrip("/")  # Remove trailing slashes from path
        excluded_paths = [p.rstrip("/") for p in excluded_paths]

        return path not in excluded_paths
        # Returns False if path is in excluded_paths

    def authorization_header(self, request=None) -> str:
        """It returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """It returns None
        """
        return None
