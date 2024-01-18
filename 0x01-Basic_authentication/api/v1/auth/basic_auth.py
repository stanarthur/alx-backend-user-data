#!/usr/bin/env python3
"""
Basic Authentication module for the API.
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic Authentication class.
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the
        Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header.

        Returns str: The Base64 part of the Authorization header.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            """Return None if authorization_header is None or not a string
            """
            return None

        auth_parts = authorization_header.split(' ')
        if len(auth_parts) != 2 or auth_parts[0] != 'Basic':
            """
            Return None if authorization_header doesn’t
            start by Basic (with a space at the end)
            """
            return None

        return auth_parts[1]
