# generated by datamodel-codegen:
#   filename:  schema/entity/data/pipeline.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, tagLabel
from ..services import pipelineService


class StatusType(Enum):
    Successful = 'Successful'
    Failed = 'Failed'
    Pending = 'Pending'


class TaskStatus(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Name of the Task.')
    executionStatus: Optional[StatusType] = Field(
        None, description='Status at a specific execution date.'
    )


class PipelineStatus(BaseModel):
    class Config:
        extra = Extra.forbid

    executionDate: Optional[basic.Timestamp] = Field(
        None, description='Date where the job was executed.'
    )
    executionStatus: Optional[StatusType] = Field(
        None, description='Status at a specific execution date.'
    )
    taskStatus: Optional[List[TaskStatus]] = Field(
        None, description='Series of task executions and its status.'
    )


class Task(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str = Field(
        ..., description='Name that identifies this task instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Task. It could be title or label from the pipeline services.',
    )
    fullyQualifiedName: Optional[str] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName.TaskName'.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of this Task.'
    )
    taskUrl: Optional[str] = Field(
        None,
        description='Task URL to visit/manage. This URL points to respective pipeline service UI.',
    )
    downstreamTasks: Optional[List[str]] = Field(
        None, description='All the tasks that are downstream of this task.'
    )
    taskType: Optional[str] = Field(
        None, description='Type of the Task. Usually refers to the class it implements.'
    )
    taskSQL: Optional[basic.SqlQuery] = Field(
        None, description='SQL used in the task. Can be used to determine the lineage.'
    )
    startDate: Optional[str] = Field(None, description='start date for the task.')
    endDate: Optional[str] = Field(None, description='end date for the task.')
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this task.'
    )


class Pipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a pipeline instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this pipeline instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Pipeline. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName'.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of this Pipeline.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    pipelineUrl: Optional[str] = Field(
        None,
        description='Pipeline  URL to visit/manage. This URL points to respective pipeline service UI.',
    )
    concurrency: Optional[int] = Field(None, description='Concurrency of the Pipeline.')
    pipelineLocation: Optional[str] = Field(None, description='Pipeline Code Location.')
    startDate: Optional[basic.DateTime] = Field(
        None, description='Start date of the workflow.'
    )
    tasks: Optional[List[Task]] = Field(
        None, description='All the tasks that are part of pipeline.'
    )
    pipelineStatus: Optional[List[PipelineStatus]] = Field(
        None, description='Series of pipeline executions and its status.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this Pipeline.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Pipeline.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this pipeline is hosted in.'
    )
    serviceType: Optional[pipelineService.PipelineServiceType] = Field(
        None, description='Service type where this pipeline is hosted in.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
