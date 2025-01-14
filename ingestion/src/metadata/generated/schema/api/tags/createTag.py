# generated by datamodel-codegen:
#   filename:  schema/api/tags/createTag.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.tags import tagCategory
from ...type import basic


class CreateTagRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: tagCategory.TagName
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this tag.'
    )
    description: basic.Markdown = Field(
        ..., description='Unique name of the tag category'
    )
    associatedTags: Optional[List[str]] = Field(
        None, description='Fully qualified names of tags associated with this tag'
    )
