# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValuesToBeInSet.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel, Extra, Field


class ColumnValuesToBeInSet(BaseModel):
    class Config:
        extra = Extra.forbid

    allowedValues: List[Union[str, float]] = Field(
        ..., description='An Array of values.'
    )
