# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValuesSumToBeBetween.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class ColumnValuesSumToBeBetween(BaseModel):
    class Config:
        extra = Extra.forbid

    minValueForColSum: Optional[int] = Field(
        None,
        description='Expected sum of values in the column to be greater or equal than',
    )
    maxValueForColSum: Optional[int] = Field(
        None, description='Expected sum values in the column to be lower or equal than'
    )
