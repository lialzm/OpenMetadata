# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/snowflakeConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class SnowflakeType(Enum):
    Snowflake = 'Snowflake'


class SnowflakeScheme(Enum):
    snowflake = 'snowflake'


class SnowflakeConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SnowflakeType] = Field(
        SnowflakeType.Snowflake, description='Service Type', title='Service Type'
    )
    scheme: Optional[SnowflakeScheme] = Field(
        SnowflakeScheme.snowflake,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to Snowflake. This user should have privileges to read all the metadata in Snowflake.',
        title='Username',
    )
    password: SecretStr = Field(
        ..., description='Password to connect to Snowflake.', title='Password'
    )
    account: str = Field(
        ...,
        description='If the Snowflake URL is https://xyz1234.us-east-1.gcp.snowflakecomputing.com, then the account is xyz1234.us-east-1.gcp',
        title='Account',
    )
    role: Optional[str] = Field(None, description='Snowflake Role.', title='Role')
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank, OpenMetadata Ingestion attempts to scan all the databases.',
        title='Database',
    )
    warehouse: str = Field(..., description='Snowflake warehouse.', title='Warehouse')
    queryTag: Optional[str] = Field(
        'OpenMetadata',
        description='Session query tag used to monitor usage on snoflake',
        title='Query Tag',
    )
    privateKey: Optional[SecretStr] = Field(
        None,
        description='Connection to Snowflake instance via Private Key',
        title='Private Key',
    )
    snowflakePrivatekeyPassphrase: Optional[SecretStr] = Field(
        None,
        description='Snowflake Passphrase Key used with Private Key',
        title='Snowflake Passphrase Key',
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
    supportsDatabase: Optional[connectionBasicType.SupportsDatabase] = Field(
        None, title='Supports Profiler'
    )