# generated by datamodel-codegen:
#   filename:  schema/metadataIngestion/mlmodelServiceMetadataPipeline.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field


class MlModelMetadataConfigType(Enum):
    MlModelMetadata = 'MlModelMetadata'


class MlModelServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[MlModelMetadataConfigType] = Field(
        MlModelMetadataConfigType.MlModelMetadata, description='Pipeline type'
    )
