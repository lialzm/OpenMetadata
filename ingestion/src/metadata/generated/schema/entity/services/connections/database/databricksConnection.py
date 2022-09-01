# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/databricksConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class DatabricksType(Enum):
    Databricks = 'Databricks'


class DatabricksScheme(Enum):
    databricks_connector = 'databricks+connector'


class DatabricksConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[DatabricksType] = Field(
        DatabricksType.Databricks, description='Service Type', title='Service Type'
    )
    scheme: Optional[DatabricksScheme] = Field(
        DatabricksScheme.databricks_connector,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: Optional[str] = Field(
        None,
        description='Username to connect to Databricks. This user should have privileges to read all the metadata in Databricks.',
        title='Username',
    )
    password: Optional[SecretStr] = Field(
        None, description='Password to connect to Databricks.', title='Password'
    )
    hostPort: str = Field(
        ...,
        description='Host and port of the Databricks service.',
        title='Host and Port',
    )
    token: SecretStr = Field(
        ..., description='Generated Token to connect to Databricks.', title='Token'
    )
    httpPath: Optional[str] = Field(
        None, description='Databricks compute resources URL.', title='Http Path'
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