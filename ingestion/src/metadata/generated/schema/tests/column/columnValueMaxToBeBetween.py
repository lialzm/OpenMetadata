# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValueMaxToBeBetween.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class ColumnValueMaxToBeBetween(BaseModel):
    class Config:
        extra = Extra.forbid

    minValueForMaxInCol: Optional[int] = Field(
        None,
        description='Expected maximum value in the column to be greater or equal than',
    )
    maxValueForMaxInCol: Optional[int] = Field(
        None,
        description='Expected maximum value in the column to be lower or equal than',
    )
