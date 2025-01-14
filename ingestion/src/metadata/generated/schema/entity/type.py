# generated by datamodel-codegen:
#   filename:  schema/entity/type.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field, constr

from ..type import basic, entityHistory, entityReference


class Category(Enum):
    field = 'field'
    entity = 'entity'


class PropertyName(BaseModel):
    __root__: constr(regex=r'^[a-z][a-zA-Z0-9]+$') = Field(
        ...,
        description='Name of the entity property. Note a property name must be unique for an entity. Property name must follow camelCase naming adopted by openMetadata - must start with lower case with no space, underscore, or dots.',
    )


class TypeName(BaseModel):
    __root__: constr(regex=r'^[a-z][a-zA-Z0-9]+$') = Field(
        ...,
        description='Name of the property or entity types. Note a property name must be unique for an entity. Property name must follow camelCase naming adopted by openMetadata - must start with lower case with no space, underscore, or dots.',
    )


class CustomProperty(BaseModel):
    class Config:
        extra = Extra.forbid

    name: PropertyName = Field(
        ...,
        description='Name of the entity property. Note a property name must be unique for an entity. Property name must follow camelCase naming adopted by openMetadata - must start with lower case with no space, underscore, or dots.',
    )
    description: basic.Markdown
    propertyType: entityReference.EntityReference = Field(
        ...,
        description='Reference to a property type. Only property types are allowed and entity types are not allowed as custom properties to extend an existing entity',
    )


class Type(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of the type instance.'
    )
    name: TypeName = Field(..., description='Unique name that identifies the type.')
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this type.'
    )
    description: basic.Markdown = Field(
        ..., description='Optional description of entity.'
    )
    category: Optional[Category] = None
    nameSpace: Optional[str] = Field(
        'custom',
        description='Namespace or group to which this type belongs to. For example, some of the property types commonly used can come from `basic` namespace. Some of the entities such as `table`, `database`, etc. come from `data` namespace.',
    )
    schema_: Optional[basic.JsonSchema] = Field(
        None,
        alias='schema',
        description='JSON schema encoded as string that defines the type. This will be used to validate the type values.',
    )
    customProperties: Optional[List[CustomProperty]] = Field(
        None,
        description='Custom properties added to extend the entity. Only available for entity type',
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
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
