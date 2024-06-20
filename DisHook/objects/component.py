from typing import List, Optional, Union, Dict
from dataclasses import dataclass, field

from .emoji import ComponentPartialEmoji

@dataclass
class Component:
    """
        Represents a component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#component-object

        Args:
            type (int): The type of the component.
    """
    type: int

    def __dict__(self) -> Dict[str, Union[int]]:
        """
        Returns the dictionary representation of the component.

        Returns:
            dict: The dictionary representation of the component.
        """
        return {
            "type": self.type
        }

@dataclass
class ActionRow(Component):
    """
        Represents an Action Row component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#action-row-object

        Args:
            components (List[Union['Button', 'StringSelect', 'TextInput', 'UserSelect', 'RoleSelect', 'MentionableSelect', 'ChannelSelect']]): The components within the Action Row.
    """
    components: List[Union['Button', 'StringSelect', 'TextInput', 'UserSelect', 'RoleSelect', 'MentionableSelect', 'ChannelSelect']]
    type: int = field(init=False, default=1)

    def __dict__(self) -> Dict[str, Union[int, List]]:
        """
        Returns the dictionary representation of the Action Row component.

        Returns:
            dict: The dictionary representation of the Action Row component.
        """
        return {
            "type": self.type,
            "components": [component.__dict__() for component in self.components]
        }

@dataclass
class Button(Component):
    """
        Represents a Button component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#button-object

        Args:
            style (int): The style of the button.
            custom_id (Optional[str]): The custom identifier for the button.
            label (Optional[str]): The label text for the button.
            emoji (Optional[ComponentPartialEmoji]): The emoji for the button.
            url (Optional[str]): The URL for the button (if style is Link).
            disabled (Optional[bool]): Whether the button is disabled. Defaults to False.
    """
    style: int
    label: Optional[str] = None
    emoji: Optional[ComponentPartialEmoji] = None
    custom_id: Optional[str] = None
    url: Optional[str] = None
    disabled: Optional[bool] = None
    type: int = field(init=False, default=2)

    def __dict__(self) -> Dict[str, Union[int, Optional[str], Optional[Dict[str, Union[str, int]]], Optional[bool]]]:
        """
        Returns the dictionary representation of the Button component.

        Returns:
            dict: The dictionary representation of the Button component.
        """
        button_dict = {
            "type": self.type,
            "style": self.style,
            "label": self.label,
            "custom_id": self.custom_id,
            "url": self.url,
            "disabled": self.disabled
        }
        if self.emoji:
            button_dict["emoji"] = self.emoji.__dict__()
        return button_dict

@dataclass
class StringSelect(Component):
    """
        Represents a String Select component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#select-menu-object

        Args:
            custom_id (str): The custom identifier for the select menu.
            options (List[Dict[str, Union[str, int]]]): The options for the select menu.
            placeholder (Optional[str]): The placeholder text for the select menu.
            min_values (Optional[int]): The minimum number of items that must be chosen.
            max_values (Optional[int]): The maximum number of items that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
    """
    custom_id: str
    options: List[Dict[str, Union[str, int]]]
    placeholder: Optional[str]
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __post_init__(self):
        super().__init__(type=3)

    def __dict__(self) -> Dict[str, Union[int, str, List[Dict[str, Union[str, int]]], Optional[bool]]]:
        """
        Returns the dictionary representation of the String Select component.

        Returns:
            dict: The dictionary representation of the String Select component.
        """
        return {
            "type": self.type,
            "custom_id": self.custom_id,
            "options": self.options,
            "placeholder": self.placeholder,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "disabled": self.disabled
        }

@dataclass
class TextInput(Component):
    """
        Represents a Text Input component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#text-input-object

        Args:
            custom_id (str): The custom identifier for the text input.
            style (int): The style of the text input.
            label (str): The label text for the text input.
            min_length (Optional[int]): The minimum length of the input.
            max_length (Optional[int]): The maximum length of the input.
            placeholder (Optional[str]): The placeholder text for the text input.
            required (Optional[bool]): Whether the text input is required. Defaults to False.
            value (Optional[str]): The initial value of the text input.
    """
    custom_id: str
    style: int
    label: str
    min_length: Optional[int]
    max_length: Optional[int]
    placeholder: Optional[str]
    required: Optional[bool]
    value: Optional[str]

    def __post_init__(self):
        super().__init__(type=4)

    def __dict__(self) -> Dict[str, Union[int, str, Optional[int], Optional[str], Optional[bool]]]:
        """
        Returns the dictionary representation of the Text Input component.

        Returns:
            dict: The dictionary representation of the Text Input component.
        """
        return {
            "type": self.type,
            "custom_id": self.custom_id,
            "style": self.style,
            "label": self.label,
            "min_length": self.min_length,
            "max_length": self.max_length,
            "placeholder": self.placeholder,
            "required": self.required,
            "value": self.value
        }

@dataclass
class UserSelect(Component):
    """
        Represents a User Select component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#select-menu-object

        Args:
            custom_id (str): The custom identifier for the select menu.
            min_values (Optional[int]): The minimum number of users that must be chosen.
            max_values (Optional[int]): The maximum number of users that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
    """
    custom_id: str
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __post_init__(self):
        super().__init__(type=5)

    def __dict__(self) -> Dict[str, Union[int, str, Optional[int], Optional[bool]]]:
        """
        Returns the dictionary representation of the User Select component.

        Returns:
            dict: The dictionary representation of the User Select component.
        """
        return {
            "type": self.type,
            "custom_id": self.custom_id,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "disabled": self.disabled
        }

@dataclass
class RoleSelect(Component):
    """
        Represents a Role Select component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#component-object-component-types

        Args:
            custom_id (str): The custom identifier for the select menu.
            min_values (Optional[int]): The minimum number of roles that must be chosen.
            max_values (Optional[int]): The maximum number of roles that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
    """
    custom_id: str
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __post_init__(self):
        super().__init__(type=6)

    def __dict__(self) -> Dict[str, Union[int, str, Optional[int], Optional[bool]]]:
        """
        Returns the dictionary representation of the Role Select component.

        Returns:
            dict: The dictionary representation of the Role Select component.
        """
        return {
            "type": self.type,
            "custom_id": self.custom_id,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "disabled": self.disabled
        }

@dataclass
class MentionableSelect(Component):
    """
        Represents a Mentionable Select component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components#select-menu-object

        Args:
            custom_id (str): The custom identifier for the select menu.
            min_values (Optional[int]): The minimum number of mentionables that must be chosen.
            max_values (Optional[int]): The maximum number of mentionables that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
    """
    custom_id: str
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __post_init__(self):
        super().__init__(type=7)

    def __dict__(self) -> Dict[str, Union[int, str, Optional[int], Optional[bool]]]:
        """
        Returns the dictionary representation of the Mentionable Select component.

        Returns:
            dict: The dictionary representation of the Mentionable Select component.
        """
        return {
            "type": self.type,
            "custom_id": self.custom_id,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "disabled": self.disabled
        }

@dataclass
class ChannelSelect(Component):
    """
        Represents a Channel Select component in a Discord message.
        - https://discord.com/developers/docs/interactions/message-components

        Args:
            custom_id (str): The custom identifier for the select menu.
            channel_types (Optional[List[str]]): The channel types to include in the select menu.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
    """
    custom_id: str
    channel_types: Optional[List[str]]
    disabled: Optional[bool]

    def __post_init__(self):
        super().__init__(type=8)

    def __dict__(self) -> Dict[str, Union[int, str, Optional[List[str]], Optional[bool]]]:
        """
        Returns the dictionary representation of the Channel Select component.

        Returns:
            dict: The dictionary representation of the Channel Select component.
        """
        return {
            "type": self.type,
            "custom_id": self.custom_id,
            "channel_types": self.channel_types,
            "disabled": self.disabled
        }
