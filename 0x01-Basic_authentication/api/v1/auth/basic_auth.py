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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string.

        Returns str: The decoded value.
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            """
            Return None if base64_authorization_header is None
            or not a str
            """
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            """
            Return None if base64_authorization_header
            is not a valid Base64
            """
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
            The decoded Base64 Authorization header.

        Returns:
            tuple: A tuple containing user email and password.
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ':' not in decoded_base64_authorization_header):
            """
            Return None, None if decoded_base64_authorization_header is None,
            not a string, or doesn't contain : character or : is the first or
            last character of decoded_base64_authorization_header
            """
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(
                                                                        ':', 1)
        return user_email, user_password
