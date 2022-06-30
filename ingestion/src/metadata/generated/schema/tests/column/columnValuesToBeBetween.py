# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValuesToBeBetween.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class ColumnValuesToBeBetween(BaseModel):
    class Config:
        extra = Extra.forbid

    minValue: Optional[int] = Field(
        None,
        description='The {minValue} value for the column entry. If minValue is not included, maxValue is treated as upperBound and there will be no minimum number of rows',
    )
    maxValue: Optional[int] = Field(
        None,
        description='The {maxValue} value for the column entry. if maxValue is not included, minValue is treated as lowerBound and there will eb no maximum number of rows',
    )
