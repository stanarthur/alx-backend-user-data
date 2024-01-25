#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt


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
