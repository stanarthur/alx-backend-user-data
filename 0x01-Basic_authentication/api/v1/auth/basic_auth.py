#!/usr/bin/env python3
"""
Basic Authentication module for the API.
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """
        Returns the User instance based on user email and password.

        Args:
            user_email (str): The user email.
            user_pwd (str): The user password.

        Returns:
            User: The User instance.
        """
        if (user_email is None or
                not isinstance(user_email, str) or
                user_pwd is None or
                not isinstance(user_pwd, str)):
            """
            Return None if user_email or user_pwd is None or not a string
            """
            return None

        users = User.search({"email": user_email})
        if not users:
            """
            Return None if the database doesn’t contain any User instance with
            email equal to user_email
            """
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            """
            Return None if user_pwd is not the password of the
            User instance found
            """
            return None

        return user

    def current_user(self, request=None) -> User:
        """
        Retrieves the User instance for a request.

        Args:
            request: The Flask request object.

        Returns:
            User: The User instance.
        """
        authorization_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            authorization_header)

        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)

        if decoded_auth_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(
                                            decoded_auth_header)

        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
