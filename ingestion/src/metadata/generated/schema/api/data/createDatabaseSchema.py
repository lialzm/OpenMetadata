# generated by datamodel-codegen:
#   filename:  schema/api/data/createDatabaseSchema.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityReference


class CreateDatabaseSchemaRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies this database schema instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this database schema.'
    )
    description: Optional[basic.Markdown] = Field(
        None,
        description='Description of the schema instance. What it has and how to use it.',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this schema'
    )
    database: entityReference.EntityReference = Field(
        ..., description='Link to the database where this schema is hosted in'
    )
