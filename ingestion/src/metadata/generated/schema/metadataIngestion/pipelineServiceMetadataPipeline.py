# generated by datamodel-codegen:
#   filename:  schema/metadataIngestion/pipelineServiceMetadataPipeline.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import filterPattern


class PipelineMetadataConfigType(Enum):
    PipelineMetadata = 'PipelineMetadata'


class PipelineServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[PipelineMetadataConfigType] = Field(
        PipelineMetadataConfigType.PipelineMetadata, description='Pipeline type'
    )
    includeLineage: Optional[bool] = Field(
        True,
        description='Optional configuration to turn off fetching lineage from pipelines.',
    )
    pipelineFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None, description='Regex exclude pipelines.'
    )
