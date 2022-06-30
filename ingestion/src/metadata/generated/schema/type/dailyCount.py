# generated by datamodel-codegen:
#   filename:  schema/type/dailyCount.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field, conint

from . import basic


class DailyCountOfSomeMeasurement(BaseModel):
    class Config:
        extra = Extra.forbid

    count: conint(ge=0) = Field(
        ..., description='Daily count of a measurement on the given date.'
    )
    date: basic.Date
