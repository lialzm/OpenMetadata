# generated by datamodel-codegen:
#   filename:  schema/api/data/createMlModel.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import mlmodel
from ...type import basic, entityReference, tagLabel


class CreateMlModelRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies this ML model.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this ML model. It could be title or label from the source services',
    )
    description: Optional[basic.Markdown] = Field(
        None,
        description='Description of the ML model instance. How it was trained and for what it is used.',
    )
    algorithm: str = Field(..., description='Algorithm used to train the ML Model')
    mlFeatures: Optional[List[mlmodel.MlFeature]] = Field(
        None, description='Features used to train the ML Model.'
    )
    target: Optional[basic.EntityName] = Field(
        None, description='For supervised ML Models, the value to estimate.'
    )
    mlHyperParameters: Optional[List[mlmodel.MlHyperParameter]] = Field(
        None, description='Hyper Parameters used to train the ML Model.'
    )
    dashboard: Optional[entityReference.EntityReference] = Field(
        None, description='Performance Dashboard URL to track metric evolution'
    )
    mlStore: Optional[mlmodel.MlStore] = Field(
        None,
        description='Location containing the ML Model. It can be a storage layer and/or a container repository.',
    )
    server: Optional[basic.Href] = Field(
        None,
        description='Endpoint that makes the ML Model available, e.g,. a REST API serving the data or computing predictions.',
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this ML Model'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this database'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to the pipeline service where this pipeline is hosted in'
    )