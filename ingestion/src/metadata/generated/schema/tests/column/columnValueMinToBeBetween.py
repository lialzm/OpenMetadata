# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValueMinToBeBetween.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class ColumnValueMinToBeBetween(BaseModel):
    class Config:
        extra = Extra.forbid

    minValueForMinInCol: Optional[int] = Field(
        None,
        description='Expected minimum value in the column to be greater or equal than',
    )
    maxValueForMinInCol: Optional[int] = Field(
        None, description='Expect minimum value in the column to be lower or equal than'
    )