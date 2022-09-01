# generated by datamodel-codegen:
#   filename:  schema/security/credentials/awsCredentials.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, SecretStr


class AWSCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

    awsAccessKeyId: Optional[str] = Field(
        None, description='AWS Access key ID.', title='AWS Access Key ID'
    )
    awsSecretAccessKey: Optional[SecretStr] = Field(
        None, description='AWS Secret Access Key.', title='AWS Secret Access Key'
    )
    awsRegion: str = Field(..., description='AWS Region', title='AWS Region')
    awsSessionToken: Optional[str] = Field(
        None, description='AWS Session Token.', title='AWS Session Token'
    )
    endPointURL: Optional[str] = Field(
        None, description='EndPoint URL for the AWS', title='Endpoint URL'
    )