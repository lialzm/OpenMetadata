# generated by datamodel-codegen:
#   filename:  schema/api/lineage/addLineage.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityLineage


class AddLineageRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    description: Optional[basic.Markdown] = Field(
        None, description='User provided description of the lineage details.'
    )
    edge: entityLineage.EntitiesEdge = Field(..., description='Lineage edge details.')
