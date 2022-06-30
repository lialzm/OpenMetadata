# generated by datamodel-codegen:
#   filename:  schema/type/profile.json
#   timestamp: 2022-06-30T10:31:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra


class ImageList(BaseModel):
    class Config:
        extra = Extra.forbid

    image: Optional[AnyUrl] = None
    image24: Optional[AnyUrl] = None
    image32: Optional[AnyUrl] = None
    image48: Optional[AnyUrl] = None
    image72: Optional[AnyUrl] = None
    image192: Optional[AnyUrl] = None
    image512: Optional[AnyUrl] = None


class Profile(BaseModel):
    class Config:
        extra = Extra.forbid

    images: Optional[ImageList] = None
