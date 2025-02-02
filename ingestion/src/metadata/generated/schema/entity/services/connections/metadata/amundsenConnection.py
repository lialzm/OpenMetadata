# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/metadata/amundsenConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr

from .. import connectionBasicType


class AmundsenType(Enum):
    Amundsen = 'Amundsen'


class AmundsenConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AmundsenType] = Field(
        AmundsenType.Amundsen, description='Service Type'
    )
    username: Optional[str] = Field(
        None, description='username to connect to the Amundsen Neo4j Connection.'
    )
    password: Optional[SecretStr] = Field(
        None, description='password to connect to the Amundsen Neo4j Connection.'
    )
    hostPort: Optional[str] = Field(
        None, description='Host and port of the Amundsen Neo4j Connection.'
    )
    maxConnectionLifeTime: Optional[int] = Field(
        '50',
        description='Maximum connection lifetime for the Amundsen Neo4j Connection.',
    )
    validateSSL: Optional[bool] = Field(
        'false', description='Enable SSL validation for the Amundsen Neo4j Connection.'
    )
    encrypted: Optional[bool] = Field(
        'false', description='Enable encryption for the Amundsen Neo4j Connection.'
    )
    modelClass: Optional[str] = Field(
        None, description='Model Class for the Amundsen Neo4j Connection.'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = None
