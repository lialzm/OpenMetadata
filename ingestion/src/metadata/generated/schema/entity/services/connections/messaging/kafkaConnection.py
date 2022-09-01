# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/messaging/kafkaConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from .. import connectionBasicType


class KafkaType(Enum):
    Kafka = 'Kafka'


class KafkaConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[KafkaType] = Field(
        KafkaType.Kafka, description='Service Type', title='Service Type'
    )
    bootstrapServers: str = Field(
        ...,
        description='Kafka bootstrap servers. add them in comma separated values ex: host1:9092,host2:9092',
        title='Bootstrap Servers',
    )
    schemaRegistryURL: Optional[AnyUrl] = Field(
        None,
        description='Confluent Kafka Schema Registry URL.',
        title='Schema Registry URL',
    )
    consumerConfig: Optional[Dict[str, Any]] = Field(
        {}, description='Confluent Kafka Consumer Config', title='Consumer Config'
    )
    schemaRegistryConfig: Optional[Dict[str, Any]] = Field(
        {},
        description='Confluent Kafka Schema Registry Config.',
        title='Schema Registry Config',
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')