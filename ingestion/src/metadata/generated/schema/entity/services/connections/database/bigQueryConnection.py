# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/bigQueryConnection.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .....security.credentials import gcsCredentials
from .. import connectionBasicType


class BigqueryType(Enum):
    BigQuery = 'BigQuery'


class BigqueryScheme(Enum):
    bigquery = 'bigquery'


class BigQueryConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[BigqueryType] = Field(
        BigqueryType.BigQuery, description='Service Type', title='Service Type'
    )
    scheme: Optional[BigqueryScheme] = Field(
        BigqueryScheme.bigquery,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    hostPort: Optional[str] = Field(
        'bigquery.googleapis.com',
        description='BigQuery APIs URL.',
        title='Host and Port',
    )
    credentials: gcsCredentials.GCSCredentials = Field(
        ..., description='GCS Credentials', title='GCS Credentials'
    )
    tagCategoryName: Optional[str] = Field(
        'BigqueryPolicyTags',
        description='Custom OpenMetadata Tag category name for BigQuery policy tags.',
        title='Tag Category Name',
    )
    partitionQueryDuration: Optional[int] = Field(
        1,
        description='Duration for partitioning BigQuery tables.',
        title='Partition Query Duration',
    )
    partitionQuery: Optional[str] = Field(
        'select * from {}.{} WHERE {} = "{}" LIMIT 1000',
        description='Partitioning query for BigQuery tables.',
        title='Partition Query',
    )
    partitionField: Optional[str] = Field(
        '_PARTITIONTIME',
        description='Column name on which the BigQuery table will be partitioned.',
        title='Partition Field',
    )
    taxonomyLocation: Optional[str] = Field(
        'us',
        description='Taxonomy location used to fetch policy tags',
        title='Taxonomy Location',
    )
    usageLocation: Optional[str] = Field(
        'us',
        description='Location used to query INFORMATION_SCHEMA.JOBS_BY_PROJECT to fetch usage data. You can pass multi-regions, such as `us` or `eu`, or you specific region. Australia and Asia multi-regions are not yet in GA.',
        title='Usage Location',
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
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
