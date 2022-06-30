# generated by datamodel-codegen:
#   filename:  schema/api/data/createGlossary.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import glossary
from ...type import basic, entityReference, tagLabel


class CreateGlossaryRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: glossary.Name = Field(..., description='Name that identifies this glossary.')
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this glossary.'
    )
    description: basic.Markdown = Field(
        ..., description='Description of the glossary instance.'
    )
    reviewers: Optional[List[entityReference.EntityReference]] = Field(
        None, description='User references of the reviewers for this glossary.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this glossary'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this glossary'
    )
