# generated by datamodel-codegen:
#   filename:  schema/security/client/azureSSOClientConfig.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Extra, Field


class AzureSSOClientConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    clientSecret: str = Field(..., description='Azure SSO client secret key')
    authority: str = Field(..., description='Azure SSO Authority')
    clientId: str = Field(..., description='Azure Client ID.')
    scopes: List[str] = Field(..., description='Azure Client ID.')
