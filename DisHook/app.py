from typing import List, Optional
import requests

from .objects.poll import Poll
from .exceptions import EmptyWebhook
from .objects.embed import Embed
from .objects.allowed_mentions import AllowedMentions

class Webhook(object):
    """
        Represents a Discord webhook.
        - https://discord.com/developers/docs/resources/webhook
    """
    webhook_url: str
    wait: Optional[bool]
    thread_id: Optional[int]
    tts: Optional[bool]
    formed_url: str
    allowed_mentions: Optional[AllowedMentions]
    username: Optional[str]
    avatar_url: Optional[str]
    content: Optional[str]
    embeds: List[Embed]
    components: List[object]
    files: Optional[object]
    poll: Optional[Poll]

    def __init__(self, webhook_url: str, wait: Optional[bool] = False, thread_id: Optional[int] = None, tts: Optional[bool] = False) -> None:
        """
            Initializes the webhook.

            Args:
                webhook_url (str): The URL of the webhook.
                wait (Optional[bool], optional): Whether to wait for the message to be sent before relaying a response. Defaults to False.
                thread_id (Optional[int], optional): The thread ID to send the message to. Defaults to None.
                tts (Optional[bool], optional): Whether the message is text-to-speech. Defaults to False.
        """
        self.webhook_url = webhook_url
        self.wait = wait
        self.thread_id = thread_id
        self.tts = tts

        self.formed_url = f"{self.webhook_url}?wait={'true' if self.wait else 'false'}{'&thread_id=' + self.thread_id if self.thread_id else ''}"

        self.allowed_mentions = None

        self.username = None
        self.avatar_url = None

        self.content = None
        self.embeds = []
        self.components = []
        self.files = None  # should be an object
        self.poll = None  # should be an object

    def add_embed(self, embed: Embed) -> None:
        """
            Adds an [embed](https://discord.com/developers/docs/resources/channel#embed-object) to the webhook.

            Args:
                embed (DisHook.Embed): The embed to add.
        """
        if len(self.embeds) < 10:
            self.embeds.append(embed)
            self.validate()  # Re-validate after adding an embed
        else:
            raise ValueError("Maximum of 10 embeds are allowed.")
    
    def add_poll(self, poll: Poll) -> None:
        """
            Adds a [poll](https://discord.com/developers/docs/resources/poll#poll-object) to the webhook.

            Args:
                poll (DisHook.Poll): The poll to add.
        """
        self.poll = poll
    
    def add_component(self, component: object) -> None:
        """
            Adds a [DisHook.component](https://discord.com/developers/docs/interactions/message-components) to the webhook. This feature is only available for webhooks that are 'application owned' (i.e. created by a bot user).
            
            Args:
                component (object): The component to add.
        """
        self.components.append(component.__dict__())

    def set_content(self, content: str) -> None:
        """
            Sets the content of the webhook.

            Args:
                content (str): The content to set.
        """
        if len(content) > 2000:
            raise ValueError("Content length cannot exceed 2000 characters.")
        self.content = content

    def set_user(self, username: str, avatar_url: str) -> None:
        """
            Sets the username and avatar URL of the webhook.

            Args:
                username (str): The username to set.
                avatar_url (str): The avatar URL to set.
        """
        self.username = username
        self.avatar_url = avatar_url
    
    def set_allowed_mentions(self, allowed_mentions: AllowedMentions) -> None:
        """
            Sets the [allowed mentions](https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mention-types) of the webhook.

            Args:
                allowed_mentions (DisHook.AllowedMentions): The allowed mentions to set.
        """
        self.allowed_mentions = allowed_mentions

    def validate(self) -> None:
        """
            Validates the webhook, as per the [Discord embed limits](https://discord.com/developers/docs/resources/channel#embed-object-embed-limits).

            Raises:
                ValueError: If the webhook is invalid.
        """
        total_chars = sum((len(embed.title or "") + len(embed.description or "") +
                           sum(len(field.name) for field in embed.fields) +
                           sum(len(field.value) for field in embed.fields) +
                           (len(embed.footer.text) if embed.footer and embed.footer.text else 0) +
                           (len(embed.author.name) if embed.author and embed.author.name else 0))
                          for embed in self.embeds)
        
        if total_chars > 6000:
            raise ValueError("Combined characters in title, description, fields, footer text, and author name across all embeds cannot exceed 6000.")

    def send(self) -> requests.Response:
        """
            Sends the webhook.

            Returns:
                requests.Response: The webhook response from Discord.
        """
        if not self.content and not self.embeds and not self.components and not self.file and not self.poll:
            raise EmptyWebhook("Webhook must have content, embeds, components, file, or poll.")
        data = {
            "content": self.content,
            "username": self.username,
            "avatar_url": self.avatar_url,
            "tts": self.tts,

            "embeds": [embed.__dict__() for embed in self.embeds],
            "allowed_mentions": self.allowed_mentions.__dict__() if self.allowed_mentions else None,

            "components": self.components,
            "files": self.files if self.files else None,
            # "payload_json": {},
            # "attachments": [self.file],
            #"flags": self.flags,
            # "applied_tags": "",
            "poll": self.poll.__dict__() if self.poll else None,
        }
        
        headers = {"Content-Type": "application/json"}
        cookies = {}
        result = requests.post(self.formed_url, json=data, headers=headers, cookies=cookies)
        
        if result.status_code == 200:
            return result
        
        if result.status_code == 429:
            raise ValueError(f"Failed to send webhook: {result.text}")
