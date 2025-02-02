# generated by datamodel-codegen:
#   filename:  schema/security/client/googleSSOClientConfig.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class GoogleSSOClientConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    secretKey: str = Field(
        ..., description='Google SSO client secret key path or contents.'
    )
    audience: Optional[str] = Field(
        'https://www.googleapis.com/oauth2/v4/token',
        description='Google SSO audience URL',
    )
