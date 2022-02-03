from datetime import datetime
from optparse import Option
from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    username: str
    discriminator: str
    avatar: str
    bot: Optional[bool] = None
    system: Optional[bool] = None
    mfa_enabled: Optional[bool] = None
    banner: Optional[str] = None
    accent_color: int = None
    locale: Optional[str] = None
    verified: Optional[bool] = None
    email: Optional[str] = None
    flags: Optional[int] = None
    premium_type: Optional[int] = None
    public_flags: Optional[int] = None

class Guild(BaseModel):
    ...

class Channel(BaseModel):
    ...

class Webhook(BaseModel):
    id: int
    type: str
    guild_id: Optional[int] = None
    channel_id: int
    user: Optional[User] = None
    name: str
    avatar: str
    token: Optional[str] = None
    application_id: int
    source_guild: Optional[Guild] = None
    source_channel: Optional[Channel] = None
    url: Optional[str] = None