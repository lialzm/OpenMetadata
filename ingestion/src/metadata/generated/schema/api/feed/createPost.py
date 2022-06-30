# generated by datamodel-codegen:
#   filename:  schema/api/feed/createPost.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class CreatePostRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    message: str = Field(
        ...,
        description='Message in markdown format. See markdown support for more details.',
    )
    from_: str = Field(
        ..., alias='from', description='Name of the User posting the message'
    )
