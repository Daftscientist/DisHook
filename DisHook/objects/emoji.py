from typing import Optional, List

class Emoji(object): # Yes, I made this before I properly read the docs. I'm not deleting it now :(
    """
    Represents an emoji.
    - https://discord.com/developers/docs/resources/emoji#emoji-object
    """
    id: Optional[int]
    name: Optional[str]
    roles: Optional[List[int]]
    user: Optional[dict]
    require_colons: Optional[bool]
    managed: Optional[bool]
    animated: Optional[bool]
    available: Optional[bool]

    def __init__(self, id: Optional[int] = None, name: Optional[str] = None,
                 roles: Optional[List[int]] = None, user: Optional[dict] = None,
                 require_colons: Optional[bool] = None, managed: Optional[bool] = None,
                 animated: Optional[bool] = None, available: Optional[bool] = None):
        """
        Initializes the emoji object.

        Args:
            id (Optional[int]): The ID of the emoji.
            name (Optional[str]): The name of the emoji.
            roles (Optional[List[int]]): Roles allowed to use this emoji.
            user (Optional[dict]): User that created this emoji.
            require_colons (Optional[bool]): Whether this emoji must be wrapped in colons.
            managed (Optional[bool]): Whether this emoji is managed.
            animated (Optional[bool]): Whether this emoji is animated.
            available (Optional[bool]): Whether this emoji can be used.
        """
        self.id = id
        self.name = name
        self.roles = roles
        self.user = user
        self.require_colons = require_colons
        self.managed = managed
        self.animated = animated
        self.available = available

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

class PartialEmoji(object):
    """
    Represents a partial emoji as required by the [Poll Media Object](https://discord.com/developers/docs/resources/poll#poll-media-object).
    - https://discord.com/developers/docs/resources/emoji#emoji-object
    """
    _id: Optional[int]
    name: Optional[str]

    def __init__(self, _id: Optional[int] = None, name: Optional[str] = None):
        if _id is None and name is None:
            raise ValueError("Either ID or name must be provided.")
        if _id is not None and name is not None:
            raise ValueError("Either ID or name must be provided, not both.")
        
        self._id = _id
        self.name = name
    
    def __dict__(self):
        if self._id:
            return {
                "id": self._id
            }
        return {
            "name": self.name
        }