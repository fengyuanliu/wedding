# coding=utf-8
"""Schemata module.

This module provides schema validation and serialisation/deserialisation for
dictionary-like objects.

"""

from marshmallow import Schema, ValidationError, fields


class AgeField(fields.Integer):
    """Field to validate age."""
    def _validate(self, value):
        """Validate age bounds"""
        super()._validate(value)
        if not 0 <= value <= 150:
            raise ValidationError('Value restricted between 0 and 150')


class BaseSchema(Schema):
    """Base schema. All schema classes should inherit from this."""
    pass


class UserSchema(BaseSchema):
    username = fields.Str(required=True)
    age = AgeField()
