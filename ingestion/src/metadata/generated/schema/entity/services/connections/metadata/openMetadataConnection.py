# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/metadata/openMetadataConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from .....security.client import (
    auth0SSOClientConfig,
    azureSSOClientConfig,
    customOidcSSOClientConfig,
    googleSSOClientConfig,
    oktaSSOClientConfig,
    openMetadataJWTClientConfig,
)
from .. import connectionBasicType


class AuthProvider(Enum):
    no_auth = 'no-auth'
    azure = 'azure'
    google = 'google'
    okta = 'okta'
    auth0 = 'auth0'
    custom_oidc = 'custom-oidc'
    openmetadata = 'openmetadata'


class OpenmetadataType(Enum):
    OpenMetadata = 'OpenMetadata'


class OpenMetadataConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[OpenmetadataType] = Field(
        OpenmetadataType.OpenMetadata, description='Service Type'
    )
    hostPort: str = Field(
        ...,
        description='OpenMetadata Server Config. Must include API end point ex: http://localhost:8585/api',
    )
    authProvider: Optional[AuthProvider] = Field(
        AuthProvider.no_auth,
        description='OpenMetadata Server Authentication Provider. Make sure configure same auth providers as the one configured on OpenMetadata server.',
    )
    securityConfig: Optional[
        Union[
            googleSSOClientConfig.GoogleSSOClientConfig,
            oktaSSOClientConfig.OktaSSOClientConfig,
            auth0SSOClientConfig.Auth0SSOClientConfig,
            azureSSOClientConfig.AzureSSOClientConfig,
            customOidcSSOClientConfig.CustomOIDCSSOClientConfig,
            openMetadataJWTClientConfig.OpenMetadataJWTClientConfig,
        ]
    ] = Field(None, description='OpenMetadata Client security configuration.')
    apiVersion: Optional[str] = Field(
        'v1', description='OpenMetadata server API version to use.'
    )
    includeTopics: Optional[bool] = Field(
        True, description='Include Topics for Indexing'
    )
    includeTables: Optional[bool] = Field(
        True, description='Include Tables for Indexing'
    )
    includeDashboards: Optional[bool] = Field(
        True, description='Include Dashboards for Indexing'
    )
    includePipelines: Optional[bool] = Field(
        True, description='Include Pipelines for Indexing'
    )
    includeMlModels: Optional[bool] = Field(
        True, description='Include MlModels for Indexing'
    )
    includeUsers: Optional[bool] = Field(True, description='Include Users for Indexing')
    includeTeams: Optional[bool] = Field(True, description='Include Teams for Indexing')
    includeGlossaryTerms: Optional[bool] = Field(
        True, description='Include Glossary Terms for Indexing'
    )
    includeTags: Optional[bool] = Field(True, description='Include Tags for Indexing')
    includePolicy: Optional[bool] = Field(True, description='Include Tags for Policy')
    includeMessagingServices: Optional[bool] = Field(
        True, description='Include Messaging Services for Indexing'
    )
    enableVersionValidation: Optional[bool] = Field(
        True, description='Validate Openmetadata Server & Client Version.'
    )
    includeDatabaseServices: Optional[bool] = Field(
        True, description='Include Database Services for Indexing'
    )
    includePipelineServices: Optional[bool] = Field(
        True, description='Include Pipeline Services for Indexing'
    )
    limitRecords: Optional[int] = Field(
        '1000', description='Limit the number of records for Indexing.'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = None
