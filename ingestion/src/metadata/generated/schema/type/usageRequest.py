# generated by datamodel-codegen:
#   filename:  schema/type/usageRequest.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class UsageRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    date: str = Field(..., description='Date of execution of SQL query')
    count: int = Field(..., description='Usage count of table')
