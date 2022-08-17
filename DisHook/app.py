""" DisHook, A lightweight  """

import json
import requests
from DisHook import embed, exceptions, helpers
from helpers import Request
from pydantic import BaseModel
from typing import List, Optional

class App(object):
    def __init__(self, webhook_url: str, default_username: str = None, default_avatar_url: str = None) -> None:
        self.default_username = default_username
        self.default_avatar = default_avatar_url
        self.webhook_url = webhook_url
    @classmethod
    def send(self, username: str = None, avatar_url: str = None, content: str = "", tts: bool=False, embeds: List[embed.Generate] = {}, allowed_mentions: helpers.AllowedMentions = {}, attachments: List[helpers.Attachment] = {}):
        internalEmbeds = []
        for item in embeds:
            internalEmbeds.append(json.loads(item.json()))
        internalAttachments = []
        for item in attachments:
            internalAttachments.append(json.loads(item.json()))
        data = {
            "username": username or self.default_username,
            "avatar_url": avatar_url or self.default_avatar,
            "content": content,
            "tts": tts,
            "embeds": internalEmbeds,
            "allowed_mentions": allowed_mentions,
            "attachments": internalAttachments
        }
        result = Request.post(self.webhook_url, "?wait=true", data)
        thing = result.json()
        return helpers.Webhook(**thing)

    def get(self, message_id: int):
        result = requests.get(f"{self.webhook_url}/messages/{message_id}")
        return helpers.Webhook(**result.json())

    def delete(self, message_id: int):
        result = requests.delete(f"{self.webhook_url}/messages/{message_id}")
        return True

    def edit(self, message_id: int, content: str = None, embeds: List[embed.Generate] = [], allowed_mentions: helpers.AllowedMentions = None, attachments: List[helpers.Attachment] = []):
        data = {
            "content": content,
            "embeds": embeds,
            "allowed_mentions": allowed_mentions,
            "attachments": attachments
        }
        result = requests.patch(f"{self.webhook_url}/messages/{message_id}", json=data)
        if result.json() == {'message': 'Cannot send an empty message', 'code': 50006}:
            raise exceptions.EmptyMessage("You can't send an empty message.")
        else:
            return self.get(message_id)