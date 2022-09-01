# generated by datamodel-codegen:
#   filename:  schema/entity/data/table.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field, confloat, constr

from ...tests import columnTest, customMetric, tableTest
from ...type import basic, entityHistory, entityReference, tagLabel, usageDetails
from ..services import databaseService


class TableType(Enum):
    Regular = 'Regular'
    External = 'External'
    View = 'View'
    SecureView = 'SecureView'
    MaterializedView = 'MaterializedView'
    Iceberg = 'Iceberg'
    Local = 'Local'


class DataType(Enum):
    NUMBER = 'NUMBER'
    TINYINT = 'TINYINT'
    SMALLINT = 'SMALLINT'
    INT = 'INT'
    BIGINT = 'BIGINT'
    BYTEINT = 'BYTEINT'
    BYTES = 'BYTES'
    FLOAT = 'FLOAT'
    DOUBLE = 'DOUBLE'
    DECIMAL = 'DECIMAL'
    NUMERIC = 'NUMERIC'
    TIMESTAMP = 'TIMESTAMP'
    TIME = 'TIME'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    INTERVAL = 'INTERVAL'
    STRING = 'STRING'
    MEDIUMTEXT = 'MEDIUMTEXT'
    TEXT = 'TEXT'
    CHAR = 'CHAR'
    VARCHAR = 'VARCHAR'
    BOOLEAN = 'BOOLEAN'
    BINARY = 'BINARY'
    VARBINARY = 'VARBINARY'
    ARRAY = 'ARRAY'
    BLOB = 'BLOB'
    LONGBLOB = 'LONGBLOB'
    MEDIUMBLOB = 'MEDIUMBLOB'
    MAP = 'MAP'
    STRUCT = 'STRUCT'
    UNION = 'UNION'
    SET = 'SET'
    GEOGRAPHY = 'GEOGRAPHY'
    ENUM = 'ENUM'
    JSON = 'JSON'
    UUID = 'UUID'


class Constraint(Enum):
    NULL = 'NULL'
    NOT_NULL = 'NOT_NULL'
    UNIQUE = 'UNIQUE'
    PRIMARY_KEY = 'PRIMARY_KEY'


class ConstraintType(Enum):
    UNIQUE = 'UNIQUE'
    PRIMARY_KEY = 'PRIMARY_KEY'
    FOREIGN_KEY = 'FOREIGN_KEY'


class TableConstraint(BaseModel):
    class Config:
        extra = Extra.forbid

    constraintType: Optional[ConstraintType] = None
    columns: Optional[List[str]] = Field(
        None, description='List of column names corresponding to the constraint.'
    )


class ColumnName(BaseModel):
    __root__: constr(min_length=1, max_length=128) = Field(
        ...,
        description='Local name (not fully qualified name) of the column. ColumnName is `-` when the column is not named in struct dataType. For example, BigQuery supports struct with unnamed fields.',
    )


class IntervalType(Enum):
    TIME_UNIT = 'TIME-UNIT'
    INTEGER_RANGE = 'INTEGER-RANGE'
    INGESTION_TIME = 'INGESTION-TIME'
    COLUMN_VALUE = 'COLUMN-VALUE'


class TablePartition(BaseModel):
    class Config:
        extra = Extra.forbid

    columns: List[str] = Field(
        ..., description='List of column names corresponding to the partition.'
    )
    intervalType: IntervalType = Field(
        ..., description='type of partition interval, example time-unit, integer-range'
    )
    interval: str = Field(
        ..., description='partition interval , example hourly, daily, monthly.'
    )


class TableData(BaseModel):
    class Config:
        extra = Extra.forbid

    columns: Optional[List[ColumnName]] = Field(
        None,
        description='List of local column names (not fully qualified column names) of the table.',
    )
    rows: Optional[List[List]] = Field(
        None, description='Data for multiple rows of the table.'
    )


class CustomMetricProfile(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Custom metric name.')
    value: Optional[float] = Field(
        None, description='Profiling results for the metric.'
    )


class Histogram(BaseModel):
    class Config:
        extra = Extra.forbid

    boundaries: Optional[List] = Field(None, description='Boundaries of Histogram.')
    frequencies: Optional[List] = Field(None, description='Frequencies of Histogram.')


class ColumnProfile(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Column Name.')
    valuesCount: Optional[float] = Field(
        None, description='Total count of the values in this column.'
    )
    valuesPercentage: Optional[float] = Field(
        None,
        description='Percentage of values in this column with respect to rowcount.',
    )
    validCount: Optional[float] = Field(
        None, description='Total count of valid values in this column.'
    )
    duplicateCount: Optional[float] = Field(
        None, description='No.of Rows that contain duplicates in a column.'
    )
    nullCount: Optional[float] = Field(
        None, description='No.of null values in a column.'
    )
    nullProportion: Optional[float] = Field(
        None, description='No.of null value proportion in columns.'
    )
    missingPercentage: Optional[float] = Field(
        None,
        description='Missing Percentage is calculated by taking percentage of validCount/valuesCount.',
    )
    missingCount: Optional[float] = Field(
        None,
        description='Missing count is calculated by subtracting valuesCount - validCount.',
    )
    uniqueCount: Optional[float] = Field(
        None, description='No. of unique values in the column.'
    )
    uniqueProportion: Optional[float] = Field(
        None, description='Proportion of number of unique values in a column.'
    )
    distinctCount: Optional[float] = Field(
        None, description='Number of values that contain distinct values.'
    )
    distinctProportion: Optional[float] = Field(
        None, description='Proportion of distinct values in a column.'
    )
    min: Optional[Union[float, int, str]] = Field(
        None, description='Minimum value in a column.'
    )
    max: Optional[Union[float, int, str]] = Field(
        None, description='Maximum value in a column.'
    )
    minLength: Optional[float] = Field(
        None, description='Minimum string length in a column.'
    )
    maxLength: Optional[float] = Field(
        None, description='Maximum string length in a column.'
    )
    mean: Optional[float] = Field(None, description='Avg value in a column.')
    sum: Optional[float] = Field(None, description='Median value in a column.')
    stddev: Optional[float] = Field(None, description='Standard deviation of a column.')
    variance: Optional[float] = Field(None, description='Variance of a column.')
    histogram: Optional[Histogram] = Field(None, description='Histogram of a column.')
    customMetricsProfile: Optional[List[CustomMetricProfile]] = Field(
        None, description='Custom Metrics profile list bound to a column.'
    )


class ModelType(Enum):
    DBT = 'DBT'


class JoinedWith(BaseModel):
    class Config:
        extra = Extra.forbid

    fullyQualifiedName: basic.FullyQualifiedEntityName
    joinCount: int


class ColumnJoins(BaseModel):
    class Config:
        extra = Extra.forbid

    columnName: Optional[ColumnName] = None
    joinedWith: Optional[List[JoinedWith]] = Field(
        None,
        description='Fully qualified names of the columns that this column is joined with.',
    )


class TableJoins(BaseModel):
    class Config:
        extra = Extra.forbid

    startDate: Optional[basic.Date] = Field(
        None, description='Date can be only from today going back to last 29 days.'
    )
    dayCount: Optional[int] = 1
    columnJoins: Optional[List[ColumnJoins]] = None
    directTableJoins: Optional[List[JoinedWith]] = Field(
        None,
        description='Joins with other tables that are not on a specific column (e.g: UNION join)',
    )


class TableProfile(BaseModel):
    class Config:
        extra = Extra.forbid

    profileDate: Optional[basic.Date] = Field(
        None, description='Data one which profile is taken.'
    )
    profileSample: Optional[confloat(le=100.0, gt=0.0)] = Field(
        None,
        description='Percentage of data used to compute this profiler execution. Represented in the range (0, 100].',
    )
    profileQuery: Optional[str] = Field(
        None,
        description="Users' raw SQL query to fetch sample data and profile the table",
    )
    columnCount: Optional[float] = Field(
        None, description='No.of columns in the table.'
    )
    rowCount: Optional[float] = Field(
        None,
        description='No.of rows in the table. This is always executed on the whole table.',
    )
    columnNames: Optional[List] = Field(None, description='List of column names')
    columnProfile: Optional[List[ColumnProfile]] = Field(
        None, description='List of local column profiles of the table.'
    )


class SqlQuery(BaseModel):
    class Config:
        extra = Extra.forbid

    query: Optional[str] = Field(
        None, description='SQL Query text that matches the table name.'
    )
    duration: Optional[float] = Field(
        None, description='How long did the query took to run in seconds.'
    )
    user: Optional[entityReference.EntityReference] = Field(
        None, description='User who ran this query.'
    )
    vote: Optional[float] = Field(
        1, description='Users can vote up to rank the popular queries.'
    )
    checksum: Optional[str] = Field(
        None, description='Checksum to avoid registering duplicate queries.'
    )
    queryDate: Optional[basic.Date] = Field(
        None, description='Date on which the query ran.'
    )


class Column(BaseModel):
    class Config:
        extra = Extra.forbid

    name: ColumnName
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this column name.'
    )
    dataType: DataType = Field(
        ..., description='Data type of the column (int, date etc.).'
    )
    arrayDataType: Optional[DataType] = Field(
        None,
        description='Data type used array in dataType. For example, `array<int>` has dataType as `array` and arrayDataType as `int`.',
    )
    dataLength: Optional[int] = Field(
        None,
        description='Length of `char`, `varchar`, `binary`, `varbinary` `dataTypes`, else null. For example, `varchar(20)` has dataType as `varchar` and dataLength as `20`.',
    )
    precision: Optional[int] = Field(
        None,
        description='The precision of a numeric is the total count of significant digits in the whole number, that is, the number of digits to both sides of the decimal point. Precision is applicable Integer types, such as `INT`, `SMALLINT`, `BIGINT`, etc. It also applies to other Numeric types, such as `NUMBER`, `DECIMAL`, `DOUBLE`, `FLOAT`, etc.',
    )
    scale: Optional[int] = Field(
        None,
        description='The scale of a numeric is the count of decimal digits in the fractional part, to the right of the decimal point. For Integer types, the scale is `0`. It mainly applies to non Integer Numeric types, such as `NUMBER`, `DECIMAL`, `DOUBLE`, `FLOAT`, etc.',
    )
    dataTypeDisplay: Optional[str] = Field(
        None,
        description='Display name used for dataType. This is useful for complex types, such as `array<int>, map<int,string>, struct<>, and union types.',
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the column.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = None
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags associated with the column.'
    )
    constraint: Optional[Constraint] = Field(
        None, description='Column level constraint.'
    )
    ordinalPosition: Optional[int] = Field(
        None, description='Ordinal position of the column.'
    )
    jsonSchema: Optional[str] = Field(
        None, description='Json schema only if the dataType is JSON else null.'
    )
    children: Optional[List[Column]] = Field(
        None,
        description='Child columns if dataType or arrayDataType is `map`, `struct`, or `union` else `null`.',
    )
    columnTests: Optional[List[columnTest.ColumnTest]] = Field(
        None, description='List of column test cases that ran against a table column.'
    )
    customMetrics: Optional[List[customMetric.CustomMetric]] = Field(
        None, description='List of Custom Metrics registered for a column.'
    )


class DataModel(BaseModel):
    class Config:
        extra = Extra.forbid

    modelType: ModelType
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the Table from the model.'
    )
    path: Optional[str] = Field(None, description='Path to sql definition file.')
    rawSql: Optional[basic.SqlQuery] = Field(
        None,
        description='This corresponds to rws SQL from `<model_name>.sql` in DBT. This might be null when SQL query need not be compiled as done in DBT.',
    )
    sql: basic.SqlQuery = Field(
        ...,
        description='This corresponds to compile SQL from `<model_name>.sql` in DBT. In cases where compilation is not necessary, this corresponds to SQL that created the table.',
    )
    upstream: Optional[List[str]] = Field(
        None,
        description='Fully qualified name of Models/tables used for in `sql` for creating this table.',
    )
    columns: Optional[List[Column]] = Field(
        None,
        description='Columns from the schema defined during modeling. In case of DBT, the metadata here comes from `schema.yaml`.',
    )
    generatedAt: Optional[basic.DateTime] = None


class Table(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(..., description='Unique identifier of this table instance.')
    name: basic.EntityName = Field(
        ..., description='Name of a table. Expected to be unique within a database.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this table. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description='Fully qualified name of a table in the form `serviceName.databaseName.tableName`.',
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of a table.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(None, description='Link to this table resource.')
    tableType: Optional[TableType] = None
    columns: List[Column] = Field(..., description='Columns in this table.')
    tableConstraints: Optional[List[TableConstraint]] = Field(
        None, description='Table constraints.'
    )
    tablePartition: Optional[TablePartition] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this table.'
    )
    databaseSchema: Optional[entityReference.EntityReference] = Field(
        None, description='Reference to database schema that contains this table.'
    )
    database: Optional[entityReference.EntityReference] = Field(
        None, description='Reference to Database that contains this table.'
    )
    service: Optional[entityReference.EntityReference] = Field(
        None, description='Link to Database service this table is hosted in.'
    )
    serviceType: Optional[databaseService.DatabaseServiceType] = Field(
        None, description='Service type this table is hosted in.'
    )
    location: Optional[entityReference.EntityReference] = Field(
        None, description='Reference to the Location that contains this table.'
    )
    viewDefinition: Optional[basic.SqlQuery] = Field(
        None, description='View Definition in SQL. Applies to TableType.View only.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this table.'
    )
    usageSummary: Optional[usageDetails.TypeUsedToReturnUsageDetailsOfAnEntity] = Field(
        None, description='Latest usage information for this table.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this table.'
    )
    joins: Optional[TableJoins] = Field(
        None,
        description='Details of other tables this table is frequently joined with.',
    )
    sampleData: Optional[TableData] = Field(
        None, description='Sample data for a table.'
    )
    profileSample: Optional[confloat(le=100.0, gt=0.0)] = Field(
        None,
        description='Percentage of data we want to execute the profiler and tests on. Represented in the range (0, 100).',
    )
    profileQuery: Optional[str] = Field(
        None,
        description="Users' raw SQL query to fetch sample data and profile the table",
    )
    tableProfile: Optional[List[TableProfile]] = Field(
        None, description='Data profile for a table.'
    )
    tableQueries: Optional[List[SqlQuery]] = Field(
        None, description='List of queries that ran against a table.'
    )
    tableTests: Optional[List[tableTest.TableTest]] = Field(
        None, description='List of test cases that ran against a table.'
    )
    dataModel: Optional[DataModel] = Field(
        None,
        description='This captures information about how the table is modeled. Currently only DBT model is supported.',
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    extension: Optional[basic.EntityExtension] = Field(
        None,
        description='Entity extension data with custom attributes added to the entity.',
    )


Column.update_forward_refs()