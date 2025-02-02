# generated by datamodel-codegen:
#   filename:  schema/metadataIngestion/messagingServiceMetadataPipeline.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import filterPattern


class MessagingMetadataConfigType(Enum):
    MessagingMetadata = 'MessagingMetadata'


class MessagingServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[MessagingMetadataConfigType] = Field(
        MessagingMetadataConfigType.MessagingMetadata, description='Pipeline type'
    )
    topicFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None, description='Regex to only fetch topics that matches the pattern.'
    )
    generateSampleData: Optional[bool] = Field(
        False,
        description='Option to turn on/off generating sample data during metadata extraction.',
    )
