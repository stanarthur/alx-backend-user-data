#!/bin/usr/env python3
"""An authentication module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ It returns False-path """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None-request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None-request """
        return None
