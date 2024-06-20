from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Emoji: # Yes, I made this before I properly read the docs. I'm not deleting it now :(
    """
        Represents an emoji.
        - https://discord.com/developers/docs/resources/emoji#emoji-object

        Args:
            id (Optional[int], optional): The ID of the emoji. Defaults to None.
            name (Optional[str], optional): The name of the emoji. Defaults to None.
            roles (Optional[List[int]], optional): Roles allowed to use this emoji. Defaults to None.
            user (Optional[dict], optional): User that created this emoji. Defaults to None.
            require_colons (Optional[bool], optional): Whether this emoji must be wrapped in colons. Defaults to None.
            managed (Optional[bool], optional): Whether this emoji is managed. Defaults to None.
            animated (Optional[bool], optional): Whether this emoji is animated. Defaults to None.
            available (Optional[bool], optional): Whether this emoji can be used. Defaults to None.
    """
    id: Optional[int] = None
    name: Optional[str] = None
    roles: Optional[List[int]] = None
    user: Optional[dict] = None
    require_colons: Optional[bool] = None
    managed: Optional[bool] = None
    animated: Optional[bool] = None
    available: Optional[bool] = None

    def __dict__(self):
        """
        Returns the dictionary representation of the emoji.

        Returns:
            dict: The dictionary representation of the emoji.
        """
        return {
            "id": self.id,
            "name": self.name,
            "roles": self.roles,
            "user": self.user,
            "require_colons": self.require_colons,
            "managed": self.managed,
            "animated": self.animated,
            "available": self.available
        }

@dataclass
class PollMediaPartialEmoji:
    """
        Represents a partial emoji as required by the [Poll Media Object](https://discord.com/developers/docs/resources/poll#poll-media-object).
        - https://discord.com/developers/docs/resources/emoji#emoji-object

        Args:
            _id (Optional[int], optional): The ID of the emoji. Defaults to None.
            name (Optional[str], optional): The name of the emoji. Defaults to None.
    """
    _id: Optional[int]
    name: Optional[str]

    def __post_init__(self):
        if self._id is None and self.name is None:
            raise ValueError("Either ID or name must be provided.")
        if self._id is not None and self.name is not None:
            raise ValueError("Either ID or name must be provided, not both.")
    
    def __dict__(self):
        if self._id:
            return {
                "id": self._id
            }
        return {
            "name": self.name
        }

@dataclass
class ComponentPartialEmoji:
    """
        Represents a partial emoji as required by the [Button Component Object](https://discord.com/developers/docs/interactions/message-components#button-component-object).
        - https://discord.com/developers/docs/resources/emoji

        Args:
            _id (Optional[int], optional): The ID of the emoji. Defaults to None.
            name (Optional[str], optional): The name of the emoji. Defaults to None.
            animated (Optional[bool], optional): Whether the emoji is animated. Defaults to None.
    """

    _id: Optional[int] = None
    name: Optional[str] = None
    animated: Optional[bool] = None

    def __post_init__(self):
        if self._id is None and self.name is None:
            raise ValueError("Either ID or name must be provided.")
        if self._id is not None and self.name is not None:
            raise ValueError("Either ID or name must be provided, not both.")
    
    def __dict__(self):
        if self._id:
            return {
                "id": self._id,
                "animated": self.animated
            }
        return {
            "name": self.name,
            "animated": self.animated
        }
    