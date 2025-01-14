# generated by datamodel-codegen:
#   filename:  schema/api/services/ingestionPipelines/testServiceConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from ....entity.services import (
    dashboardService,
    databaseService,
    messagingService,
    mlmodelService,
    pipelineService,
)


class ConnectionType1(Enum):
    Database = 'Database'
    Dashboard = 'Dashboard'
    Messaging = 'Messaging'
    Pipeline = 'Pipeline'
    MlModel = 'MlModel'


class TestServiceConnectionRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    connection: Optional[
        Union[
            databaseService.DatabaseConnection,
            dashboardService.DashboardConnection,
            messagingService.MessagingConnection,
            pipelineService.PipelineConnection,
            mlmodelService.MlModelConnection,
        ]
    ] = Field(None, description='Connection object.')
    connectionType: Optional[ConnectionType1] = Field(
        None,
        description='Type of database service such as MySQL, BigQuery, Snowflake, Redshift, Postgres...',
    )
