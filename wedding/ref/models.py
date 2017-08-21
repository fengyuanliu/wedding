"""Models module.

This module defines database models and utilities for interacting with them.

"""

from resting.database import db


class User(db.Model):
    """User model."""
    __tablename__ = 'user'
    username = db.Column(db.String, primary_key=True)
    age = db.Column(db.Integer)
