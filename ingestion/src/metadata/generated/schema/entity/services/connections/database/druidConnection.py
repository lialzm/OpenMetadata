# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/druidConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class DruidType(Enum):
    Druid = 'Druid'


class DruidScheme(Enum):
    druid = 'druid'


class DruidConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[DruidType] = Field(
        DruidType.Druid, description='Service Type', title='Service Type'
    )
    scheme: Optional[DruidScheme] = Field(
        DruidScheme.druid,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: Optional[str] = Field(
        None,
        description='Username to connect to Druid. This user should have privileges to read all the metadata in Druid.',
        title='Username',
    )
    password: Optional[SecretStr] = Field(
        None, description='Password to connect to Druid.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the Druid service.', title='Host and Port'
    )
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank, OpenMetadata Ingestion attempts to scan all the databases.',
        title='Database',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
