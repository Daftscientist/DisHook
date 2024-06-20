from dataclasses import dataclass
from typing import Optional
from .embed import Embed
from .allowed_mentions import AllowedMentions
from .component import Component
from .poll import Poll
from .interaction import InteractionChoices
from .enums import MessageFlags

@dataclass
class InteractionCallbackMessage:
    """
        Represents an interaction callback data object.

        Args:
            tts (Optional[bool], optional): Whether the message is text-to-speech. Defaults to False.
            content (Optional[str], optional): The content of the message. Defaults to None.
            embeds (Optional[list[Embed]], optional): The embeds of the message. Defaults to None.
            allowed_mentions (Optional[AllowedMentions], optional): The allowed mentions of the message. Defaults to None.
            flags (Optional[int], optional): The flags of the message. Defaults to None.
            components (Optional[list[Component]], optional): The components of the message. Defaults to None.
            attachments (Optional[list[object]], optional): The attachments of the message. Defaults to None.
            poll (Optional[Poll], optional): The poll of the message. Defaults to None.
    """
    tts: Optional[bool] = False
    content: Optional[str] = None
    embeds: Optional[list[Embed]] = None
    allowed_mentions: Optional[AllowedMentions] = None
    flags: Optional[int] = None
    components: Optional[list[Component]] = None
    attachments: Optional[list[object]] = None
    poll: Optional[Poll] = None

    def __dict__(self):
        """
            Returns the dictionary representation of the object.

            Returns:
                dict: The dictionary representation of the object.
        """
        return {
            "tts": self.tts,
            "content": self.content,
            "embeds": [embed.__dict__() for embed in self.embeds] if self.embeds else None,
            "allowed_mentions": self.allowed_mentions.__dict__() if self.allowed_mentions else None,
            "flags": self.flags,
            "components": [component.__dict__() for component in self.components] if self.components else None,
            "attachments": self.attachments,
            "poll": self.poll.__dict__() if self.poll else None
        }

@dataclass
class InteractionCallbackAutocomplete:
    """
        Represents an interaction callback autocomplete object.
        - https://discord.com/developers/docs/interactions/slash-commands#autocomplete-interaction-object

        Args:
            choices (list[InteractionChoices]): The choices for the autocomplete.
    """
    choices: list[InteractionChoices]

    def __dict__(self):
        """
            Returns the dictionary representation of the object.

            Returns:
                dict: The dictionary representation of the object.
        """
        return {
            "choices": [choice.__dict__() for choice in self.choices]
        }

@dataclass
class InteractionCallbackModal:
    """
        Represents an interaction callback modal object.
        - https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-modal

        Args:
            custom_id (str): The custom ID of the modal.
            title (str): The title of the modal.
            components (list[Component]): The components of the modal. Component type currently limited to type 4 (Text Input).
    """
    custom_id: str
    title: str
    components: list[Component]

    def __post_init__(self):
        if len(self.custom_id) > 100:
            raise ValueError("The 'custom_id' field must be a string with up to 100 characters.")
        if len(self.title) > 45:
            raise ValueError("The 'title' field must be a string with up to 45 characters.")
        if len(self.components) > 5:
            raise ValueError("The 'components' field must be a list with up to 5 components.")

    def __dict__(self):
        """
            Returns the dictionary representation of the object.

            Returns:
                dict: The dictionary representation of the object.
        """
        return {
            "custom_id": self.custom_id,
            "title": self.title,
            "components": [component.__dict__() for component in self.components]
        }

