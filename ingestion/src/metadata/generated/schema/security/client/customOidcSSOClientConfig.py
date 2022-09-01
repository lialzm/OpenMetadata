# generated by datamodel-codegen:
#   filename:  schema/security/client/customOidcSSOClientConfig.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class CustomOIDCSSOClientConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    clientId: str = Field(..., description='Custom OIDC Client ID.')
    secretKey: str = Field(..., description='Custom OIDC Client Secret Key.')
    tokenEndpoint: str = Field(..., description='Custom OIDC token endpoint.')