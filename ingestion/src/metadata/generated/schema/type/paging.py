# generated by datamodel-codegen:
#   filename:  schema/type/paging.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class Paging(BaseModel):
    class Config:
        extra = Extra.forbid

    before: Optional[str] = Field(
        None,
        description='Before cursor used for getting the previous page (see API pagination for details).',
    )
    after: Optional[str] = Field(
        None,
        description='After cursor used for getting the next page (see API pagination for details).',
    )
    total: int = Field(
        ..., description='Total number of entries available to page through.'
    )