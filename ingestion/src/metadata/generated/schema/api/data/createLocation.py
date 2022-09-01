# generated by datamodel-codegen:
#   filename:  schema/api/data/createLocation.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import location
from ...type import basic, entityReference, tagLabel


class CreateLocationRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies this Location.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this location.'
    )
    path: Optional[str] = Field(None, description='Location full path.')
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the location instance.'
    )
    locationType: Optional[location.LocationType] = None
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this location'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Location'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to the pipeline service where this location is used'
    )