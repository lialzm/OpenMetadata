# generated by datamodel-codegen:
#   filename:  schema/entity/bot.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import basic, entityHistory, entityReference


class Bot(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(..., description='Unique identifier of a bot instance.')
    name: basic.EntityName = Field(..., description='Name of the bot.')
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None,
        description="Name used for display purposes. Example 'FirstName LastName'.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the bot.'
    )
    botUser: entityReference.EntityReference = Field(
        ...,
        description='Bot user created for this bot on behalf of which the bot performs all the operations, such as updating description, responding on the conversation threads, etc.',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this bot.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )