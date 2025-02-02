# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/db2Connection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class Db2Type(Enum):
    Db2 = 'Db2'


class Db2Scheme(Enum):
    db2_ibm_db = 'db2+ibm_db'


class Db2Connection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[Db2Type] = Field(
        Db2Type.Db2, description='Service Type', title='Service Type'
    )
    scheme: Optional[Db2Scheme] = Field(
        Db2Scheme.db2_ibm_db,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to DB2. This user should have privileges to read all the metadata in DB2.',
        title='Username',
    )
    password: Optional[SecretStr] = Field(
        None, description='Password to connect to DB2.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the DB2 service.', title='Host and Port'
    )
    databaseSchema: Optional[str] = Field(
        None,
        description='databaseSchema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single databaseSchema. When left blank, OpenMetadata Ingestion attempts to scan all the databaseSchema.',
        title='databaseSchema',
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
