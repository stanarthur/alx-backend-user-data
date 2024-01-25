#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt
from user import User
from bcrypt import checkpw
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash the input password using bcrypt.hashpw
    """
    salt = bcrypt.gensalt()
    """Generate a random salt
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    """Hash the password with the salt
    """
    return hashed_password


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if a user's login details are valid.
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False
