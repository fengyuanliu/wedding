# coding=utf-8
"""Database module.

This module provides database access and related utilities.

Attributes:
    db (flask_sqlalchemy.SQLAlchemy): Flask-SQLAlchemy database object.

"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
