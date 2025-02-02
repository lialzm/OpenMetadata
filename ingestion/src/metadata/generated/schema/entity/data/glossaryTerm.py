# generated by datamodel-codegen:
#   filename:  schema/entity/data/glossaryTerm.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, tagLabel


class TermReference(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(
        None,
        description='Name that identifies the source of an external glossary term. Example `HealthCare.gov`.',
    )
    endpoint: Optional[AnyUrl] = Field(
        None,
        description='Name that identifies the source of an external glossary term. Example `HealthCare.gov`.',
    )


class Status(Enum):
    Draft = 'Draft'
    Approved = 'Approved'
    Deprecated = 'Deprecated'


class Name(BaseModel):
    __root__: basic.EntityName = Field(
        ..., description='Name that identifies a glossary term.'
    )


class GlossaryTerm(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of a glossary term instance.'
    )
    name: Name = Field(..., description='Preferred name for the glossary term.')
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this glossary.'
    )
    description: basic.Markdown = Field(
        ..., description='Description of the glossary term.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description='A unique name that identifies a glossary term. It captures name hierarchy of glossary of terms in the form of `glossaryName.parentTerm.childTerm`.',
    )
    synonyms: Optional[List[Name]] = Field(
        None,
        description='Alternate names that are synonyms or near-synonyms for the glossary term.',
    )
    glossary: entityReference.EntityReference = Field(
        ..., description='Glossary that this term belongs to.'
    )
    parent: Optional[entityReference.EntityReference] = Field(
        None,
        description='Parent glossary term that this term is child of. When `null` this term is the root term of the glossary.',
    )
    children: Optional[entityReference.EntityReferenceList] = Field(
        None,
        description='Other glossary terms that are children of this glossary term.',
    )
    relatedTerms: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Other glossary terms that are related to this glossary term.'
    )
    references: Optional[List[TermReference]] = Field(
        None, description='Link to a reference from an external glossary.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    reviewers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='User names of the reviewers for this glossary.'
    )
    usageCount: Optional[int] = Field(
        None,
        description="Count of how many times this and it's children glossary terms are used as labels.",
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None,
        description="Tags associated with this glossary term. These tags captures relationship of a glossary term with a tag automatically. As an example a glossary term 'User.PhoneNumber' might have an associated tag 'PII.Sensitive'. When 'User.Address' is used to label a column in a table, 'PII.Sensitive' label is also applied automatically due to Associated tag relationship.",
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    status: Optional[Status] = Field(None, description='Status of the glossary term.')
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
