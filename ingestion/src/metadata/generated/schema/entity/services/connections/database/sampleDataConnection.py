# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/sampleDataConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .. import connectionBasicType


class SampleDataType(Enum):
    SampleData = 'SampleData'


class SampleDataConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SampleDataType] = Field(
        SampleDataType.SampleData, description='Service Type', title='Service Type'
    )
    sampleDataFolder: Optional[str] = Field(None, description='Sample Data File Path')
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None