# generated by datamodel-codegen:
#   filename:  schema/entity/policies/filters.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel, Field

from ..tags import tagCategory


class Filters(BaseModel):
    __root__: Any = Field(..., title='Filters')


class Prefix(BaseModel):
    __root__: str = Field(..., description='Prefix path of the entity.')


class Regex(BaseModel):
    __root__: str = Field(..., description='Regex that matches the entity.')


class Tags(BaseModel):
    __root__: List[tagCategory.TagName] = Field(
        ..., description='Set of tags to match on (OR among all tags).'
    )
