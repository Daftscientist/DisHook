import requests
import json
from DisHook import embed, exceptions, helpers
from pydantic import BaseModel
from typing import List, Optional

class App(object):
    def __init__(self, webhook_url: str, default_username: str = None, default_avatar_url: str = None) -> None:
        self.default_username = default_username
        self.default_avatar = default_avatar_url
        self.webhook_url = webhook_url

    def send(self, username: str = None, avatar_url: str = None, content: str = "", tts: bool=False, embeds: List[embed.Generate] = {}, allowed_mentions: helpers.AllowedMentions = {}, attachments: List[helpers.Attachment] = {}):
        internalEmbeds = []
        for item in embeds:
            internalEmbeds.append(json.loads(item.json()))
        internalAttachments = []
        for item in attachments:
            internalAttachments.append(json.loads(item.json()))
        data = {
            "username": username,
            "avatar_url": avatar_url,
            "content": content,
            "tts": tts,
            "embeds": internalEmbeds,
            "allowed_mentions": allowed_mentions,
            "attachments": internalAttachments
        }
        result = requests.post(f"{self.webhook_url}?wait=true", json=data)
        if result.json() == {'message': 'Cannot send an empty message', 'code': 50006}:
            raise exceptions.EmptyMessage("You can't send an empty message.")
        else:
            thing = result.json()
        return helpers.Webhook(**thing)
