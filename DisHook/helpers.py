from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from DisHook import app, embed, exceptions
import requests

class AllowedMentions(BaseModel):
    pass

class Attachment(BaseModel):
    id: int
    filename: str
    description: Optional[str] = None
    content_type: Optional[str] = None
    size: int
    url: str
    proxy_url: str
    height: Optional[int] = None
    width: Optional[int] = None
    ephemeral: Optional[bool] = None

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

class Author(BaseModel):
    bot: bool
    id: int
    username: str
    avatar: Optional[str]
    discriminator: int

class Mentions(BaseModel):
    pass

class Tag(BaseModel):
    bot_id: str
    integration_id: str
    premium_subscriber: str

class MentionRoles(BaseModel):
    id: int
    name: str
    color: int
    hoist: bool
    icon: Optional[str]
    unicode_emoji: Optional[str]
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: Optional[List[Tag]]

class Webhook(BaseModel):        
    id: int
    type: int
    content: str
    channel_id: int
    author: Author
    attachments: Optional[List[Attachment]] = []
    embeds: Optional[List[embed.Generate]] = []
    mentions: Optional[List[Mentions]] = []
    mention_roles: Optional[List[MentionRoles]] = []
    pinned: bool
    mention_everyone: bool
    tts: bool
    timestamp: str
    edited_timestamp: Optional[str] = None
    flags: int
    components: list
    webhook_id: int

class Request():
    def post(webhookUrl: str, endpoint: str = "", data: dict = {}):
        url = webhookUrl + endpoint
        headers = {}
        cookies = {}
        result = requests.post(url, data, headers=headers, cookies=cookies)
        if result.status_code in [200]:
            return result
        else:
            raise exceptions.ErrorInRequest("Error during Discord API request: " + str(result.text))
    def get(webhookUrl: str, endpoint: str = ""):
        result = requests.get(webhookUrl + endpoint)