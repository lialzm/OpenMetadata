# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/verticaConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class VerticaType(Enum):
    Vertica = 'Vertica'


class VerticaScheme(Enum):
    vertica_vertica_python = 'vertica+vertica_python'


class VerticaConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[VerticaType] = Field(
        VerticaType.Vertica, description='Service Type', title='Service Type'
    )
    scheme: Optional[VerticaScheme] = Field(
        VerticaScheme.vertica_vertica_python,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to Vertica. This user should have privileges to read all the metadata in Vertica.',
        title='Username',
    )
    password: Optional[SecretStr] = Field(
        None, description='Password to connect to Vertica.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the Vertica service.', title='Host and Port'
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
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
