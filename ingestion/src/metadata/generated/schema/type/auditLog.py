# generated by datamodel-codegen:
#   filename:  schema/type/auditLog.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from . import basic


class Method(Enum):
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class AuditLog(BaseModel):
    class Config:
        extra = Extra.forbid

    method: Method = Field(..., description='HTTP Method used in a call.')
    responseCode: int = Field(
        ..., description='HTTP response code for the api requested.'
    )
    path: str = Field(..., description='Requested API Path.')
    userName: str = Field(..., description='Name of the user who made the API request.')
    entityId: basic.Uuid = Field(
        ..., description='Identifier of entity that was modified by the operation.'
    )
    entityType: str = Field(
        ..., description='Type of Entity that is modified by the operation.'
    )
    timestamp: Optional[basic.Timestamp] = Field(
        None,
        description='Timestamp when the API call is made in Unix epoch time milliseconds in Unix epoch time milliseconds.',
    )