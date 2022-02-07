from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from DisHook import embed

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
    avatar: str
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

"""
{'id': '940340878508195870', 'type': 0, 'content': 'test.', 'channel_id': '927846152810954763', 
'author': {'bot': True, 'id': '939948451360292894', 'username': 'daft webhook lmao', 'avatar': 'e3cba282b2980421ad44a9b0aefbaed9',
 'discriminator': '0000'}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 
 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-02-07T20:18:56.125000+00:00', 
 'edited_timestamp': None, 'flags': 0, 'components': [], 'webhook_id': '939948451360292894'}
"""

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