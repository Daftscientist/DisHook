from typing import List, Optional

class AllowedMentions:
    """
    Represents allowed mentions in a message.
    - https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mention-types
    """
    parse: Optional[List[str]]
    roles: Optional[List[int]]
    users: Optional[List[int]]
    replied_user: Optional[bool]

    def __init__(self, parse: Optional[List[str]] = None, roles: Optional[List[int]] = None,
                 users: Optional[List[int]] = None, replied_user: Optional[bool] = False):
        """
        Initializes the AllowedMentions object.

        Args:
            parse (List[str]): An array of allowed mention types to parse from the content.
            roles (Optional[List[int]]): Array of role IDs to mention (Max size of 100).
            users (Optional[List[int]]): Array of user IDs to mention (Max size of 100).
            replied_user (Optional[bool]): For replies, whether to mention the author of the message being replied to (default false).
        """
        if not parse and not roles and not users:
            raise ValueError("You must specify at least one of the allowed mention types to parse from the content.")

        self.parse = parse
        self.roles = roles
        self.users = users
        self.replied_user = replied_user

    def __dict__(self):
        """
        Returns the dictionary representation of the allowed mentions.

        Returns:
            dict: The dictionary representation of the allowed mentions.
        """
        return {
            "parse": self.parse,
            "roles": self.roles,
            "users": self.users,
            "replied_user": self.replied_user
        }
