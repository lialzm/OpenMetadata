# generated by datamodel-codegen:
#   filename:  schema/api/data/createTable.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field, confloat

from ...entity.data import table
from ...type import basic, entityReference, tagLabel


class CreateTableRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ...,
        description='Name that identifies the this entity instance uniquely. Same as id if when name is not unique',
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this table.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of entity instance.'
    )
    tableType: Optional[table.TableType] = None
    columns: List[table.Column] = Field(
        ..., description='Name of the tables in the database'
    )
    tableConstraints: Optional[List[table.TableConstraint]] = None
    tablePartition: Optional[table.TablePartition] = None
    profileSample: Optional[confloat(le=100.0, gt=0.0)] = Field(
        None,
        description='Percentage of data we want to execute the profiler and tests on. Represented in the range (0, 100].',
    )
    profileQuery: Optional[str] = Field(
        None,
        description="Users' raw SQL query to fetch sample data and profile the table",
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this entity'
    )
    databaseSchema: entityReference.EntityReference = Field(
        ..., description='Schema corresponding to this table'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this table'
    )
    viewDefinition: Optional[basic.SqlQuery] = Field(
        None, description='View Definition in SQL. Applies to TableType.View only'
    )
    extension: Optional[basic.EntityExtension] = Field(
        None,
        description='Entity extension data with custom attributes added to the entity.',
    )
