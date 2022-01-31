from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class Footer(BaseModel):
    text: str
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None

class Image(BaseModel):
    url: str
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None

class Thumbnail(BaseModel):
    url: str
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None

class Video(BaseModel):
    url: str
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None

class Provider(BaseModel):
    name: str
    url: Optional[str] = None

class Author(BaseModel):
    name: str
    url: Optional[str]
    icon_url: Optional[str] = None
    proxy_url: Optional[str] = None

class Field(BaseModel):
    name: str
    value: str
    inline: Optional[bool] = True

class Generate(BaseModel):
    title: Optional[str] = None
    type: Optional[str] = "rich"
    description: Optional[str] = None
    url: Optional[str] = None
    timestamp: Optional[datetime] = None ## fix cus timestamp aint that data type.
    color: Optional[int] = None
    footer: Optional[Footer] = {}
    image: Optional[Image] = {}
    thumbnail: Optional[Thumbnail] = {}
    video: Optional[Video] = {}
    provider: Optional[Provider] = {}
    author: Optional[Author] = {}
    fields: Optional[List[Field]] = []