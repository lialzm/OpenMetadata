# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/mlmodel/mlflowConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .. import connectionBasicType


class MlflowType(Enum):
    Mlflow = 'Mlflow'


class MlflowConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[MlflowType] = Field(
        MlflowType.Mlflow, description='Service Type', title='Service Type'
    )
    trackingUri: str = Field(
        ...,
        description='Mlflow Experiment tracking URI. E.g., http://localhost:5000',
        title='Tracking URI',
    )
    registryUri: str = Field(
        ...,
        description='Mlflow Model registry backend. E.g., mysql+pymysql://mlflow:password@localhost:3307/experiments',
        title='Registry URI',
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
