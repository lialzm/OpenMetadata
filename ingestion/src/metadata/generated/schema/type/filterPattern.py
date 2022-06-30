# generated by datamodel-codegen:
#   filename:  schema/type/filterPattern.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field


class FilterPatternModel(BaseModel):
    pass


class FilterPattern(BaseModel):
    class Config:
        extra = Extra.forbid

    includes: Optional[List[str]] = Field(
        None,
        description='List of strings/regex patterns to match and include only database entities that match.',
    )
    excludes: Optional[List[str]] = Field(
        None,
        description='List of strings/regex patterns to match and exclude only database entities that match.',
    )
