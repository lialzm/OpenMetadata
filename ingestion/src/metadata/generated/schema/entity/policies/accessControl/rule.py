# generated by datamodel-codegen:
#   filename:  schema/entity/policies/accessControl/rule.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from ....type import basic, tagLabel


class Operation(Enum):
    SuggestDescription = 'SuggestDescription'
    SuggestTags = 'SuggestTags'
    UpdateDescription = 'UpdateDescription'
    UpdateOwner = 'UpdateOwner'
    UpdateTags = 'UpdateTags'
    UpdateLineage = 'UpdateLineage'
    DecryptTokens = 'DecryptTokens'
    UpdateTeam = 'UpdateTeam'


class AccessControlRule(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str = Field(..., description='Name for this Rule.')
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    entityTypeAttr: Optional[str] = Field(
        None, description='Entity type that the rule should match on.'
    )
    entityTagAttr: Optional[tagLabel.TagFQN] = Field(
        None, description='Entity tag that the rule should match on.'
    )
    operation: Optional[Operation] = Field(None, description='Operation on the entity.')
    allow: Optional[bool] = Field(
        False, description='Allow or Deny operation on the entity.'
    )
    priority: Optional[int] = Field(
        250000, description='Priority of this rule among all rules across all policies.'
    )
    deleted: Optional[bool] = Field(False, description='Is the rule soft-deleted.')