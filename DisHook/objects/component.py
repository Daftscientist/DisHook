from typing import List, Optional, Union, Dict

class Component:
    """
    Represents a component in a Discord message.
    """
    type: int

    def __init__(self, type: int):
        """
        Initializes a component.

        Args:
            type (int): The type of the component.
        """
        self.type = type

    def __dict__(self) -> Dict[str, Union[int]]:
        """
        Returns the dictionary representation of the component.

        Returns:
            dict: The dictionary representation of the component.
        """
        return {
            "type": self.type
        }


class ActionRow(Component):
    """
    Represents an Action Row component in a Discord message.
    """
    components: List[Union['Button', 'StringSelect', 'TextInput', 'UserSelect', 'RoleSelect', 'MentionableSelect', 'ChannelSelect']]

    def __init__(self, components: List[Union['Button', 'StringSelect', 'TextInput', 'UserSelect', 'RoleSelect', 'MentionableSelect', 'ChannelSelect']]):
        """
        Initializes an Action Row component.

        Args:
            components (List[Union['Button', 'StringSelect', 'TextInput', 'UserSelect', 'RoleSelect', 'MentionableSelect', 'ChannelSelect']]): The components within the Action Row.
        """
        super().__init__(type=1)
        self.components = components

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


class Button(Component):
    """
    Represents a Button component in a Discord message.
    """
    style: int
    label: Optional[str]
    emoji: Optional[Dict[str, Union[str, int]]]
    custom_id: Optional[str]
    url: Optional[str]
    disabled: Optional[bool]

    def __init__(self, style: int, custom_id: Optional[str] = None, label: Optional[str] = None,
                 emoji: Optional[Dict[str, Union[str, int]]] = None, url: Optional[str] = None, disabled: Optional[bool] = False):
        """
        Initializes a Button component.

        Args:
            style (int): The style of the button.
            custom_id (Optional[str]): The custom identifier for the button.
            label (Optional[str]): The label text for the button.
            emoji (Optional[Dict[str, Union[str, int]]]): The emoji for the button.
            url (Optional[str]): The URL for the button (if style is Link).
            disabled (Optional[bool]): Whether the button is disabled. Defaults to False.
        """
        super().__init__(type=2)
        self.style = style
        self.label = label
        self.emoji = emoji
        self.custom_id = custom_id
        self.url = url
        self.disabled = disabled

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
            button_dict["emoji"] = self.emoji
        return button_dict


class StringSelect(Component):
    """
    Represents a String Select component in a Discord message.
    """
    custom_id: str
    options: List[Dict[str, Union[str, int]]]
    placeholder: Optional[str]
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __init__(self, custom_id: str, options: List[Dict[str, Union[str, int]]], placeholder: Optional[str] = None,
                 min_values: Optional[int] = None, max_values: Optional[int] = None, disabled: Optional[bool] = False):
        """
        Initializes a String Select component.

        Args:
            custom_id (str): The custom identifier for the select menu.
            options (List[Dict[str, Union[str, int]]]): The options for the select menu.
            placeholder (Optional[str]): The placeholder text for the select menu.
            min_values (Optional[int]): The minimum number of items that must be chosen.
            max_values (Optional[int]): The maximum number of items that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
        """
        super().__init__(type=3)
        self.custom_id = custom_id
        self.options = options
        self.placeholder = placeholder
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled

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


class TextInput(Component):
    """
    Represents a Text Input component in a Discord message.
    """
    custom_id: str
    style: int
    label: str
    min_length: Optional[int]
    max_length: Optional[int]
    placeholder: Optional[str]
    required: Optional[bool]
    value: Optional[str]

    def __init__(self, custom_id: str, label: str, style: int, min_length: Optional[int] = None, max_length: Optional[int] = None,
                 placeholder: Optional[str] = None, required: Optional[bool] = None, value: Optional[str] = None):
        """
        Initializes a Text Input component.

        Args:
            custom_id (str): The custom identifier for the text input.
            label (str): The label text for the text input.
            style (int): The style of the text input.
            min_length (Optional[int]): The minimum input length for the text input.
            max_length (Optional[int]): The maximum input length for the text input.
            placeholder (Optional[str]): The placeholder text for the text input.
            required (Optional[bool]): Whether the text input is required.
            value (Optional[str]): The pre-filled value for the text input.
        """
        super().__init__(type=4)
        self.custom_id = custom_id
        self.style = style
        self.label = label
        self.min_length = min_length
        self.max_length = max_length
        self.placeholder = placeholder
        self.required = required
        self.value = value

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


class UserSelect(Component):
    """
    Represents a User Select component in a Discord message.
    """
    custom_id: str
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __init__(self, custom_id: str, min_values: Optional[int] = None, max_values: Optional[int] = None, disabled: Optional[bool] = False):
        """
        Initializes a User Select component.

        Args:
            custom_id (str): The custom identifier for the select menu.
            min_values (Optional[int]): The minimum number of users that must be chosen.
            max_values (Optional[int]): The maximum number of users that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
        """
        super().__init__(type=5)
        self.custom_id = custom_id
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled

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


class RoleSelect(Component):
    """
    Represents a Role Select component in a Discord message.
    """
    custom_id: str
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __init__(self, custom_id: str, min_values: Optional[int] = None, max_values: Optional[int] = None, disabled: Optional[bool] = False):
        """
        Initializes a Role Select component.

        Args:
            custom_id (str): The custom identifier for the select menu.
            min_values (Optional[int]): The minimum number of roles that must be chosen.
            max_values (Optional[int]): The maximum number of roles that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
        """
        super().__init__(type=6)
        self.custom_id = custom_id
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled

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


class MentionableSelect(Component):
    """
    Represents a Mentionable Select component in a Discord message.
    """
    custom_id: str
    min_values: Optional[int]
    max_values: Optional[int]
    disabled: Optional[bool]

    def __init__(self, custom_id: str, min_values: Optional[int] = None, max_values: Optional[int] = None, disabled: Optional[bool] = False):
        """
        Initializes a Mentionable Select component.

        Args:
            custom_id (str): The custom identifier for the select menu.
            min_values (Optional[int]): The minimum number of mentionables that must be chosen.
            max_values (Optional[int]): The maximum number of mentionables that can be chosen.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
        """
        super().__init__(type=7)
        self.custom_id = custom_id
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled

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


class ChannelSelect(Component):
    """
    Represents a Channel Select component in a Discord message.
    """
    custom_id: str
    channel_types: Optional[List[str]]
    disabled: Optional[bool]

    def __init__(self, custom_id: str, channel_types: Optional[List[str]] = None, disabled: Optional[bool] = False):
        """
        Initializes a Channel Select component.

        Args:
            custom_id (str): The custom identifier for the select menu.
            channel_types (Optional[List[str]]): The channel types to include in the select menu.
            disabled (Optional[bool]): Whether the select menu is disabled. Defaults to False.
        """
        super().__init__(type=8)
        self.custom_id = custom_id
        self.channel_types = channel_types
        self.disabled = disabled

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
