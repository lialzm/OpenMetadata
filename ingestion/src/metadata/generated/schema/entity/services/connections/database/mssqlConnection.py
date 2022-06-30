# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/mssqlConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class MssqlType(Enum):
    Mssql = 'Mssql'


class MssqlScheme(Enum):
    mssql_pyodbc = 'mssql+pyodbc'
    mssql_pytds = 'mssql+pytds'
    mssql_pymssql = 'mssql+pymssql'


class MssqlConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[MssqlType] = Field(
        MssqlType.Mssql, description='Service Type', title='Service Type'
    )
    scheme: Optional[MssqlScheme] = Field(
        MssqlScheme.mssql_pytds,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to MSSQL. This user should have privileges to read all the metadata in MsSQL.',
        title='Username',
    )
    password: Optional[SecretStr] = Field(
        None, description='Password to connect to MSSQL.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the MSSQL service.', title='Host and Port'
    )
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank, OpenMetadata Ingestion attempts to scan all the databases.',
        title='Database',
    )
    uriString: Optional[str] = Field(
        None, description='Connection URI In case of pyodbc', title='URI String'
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
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
