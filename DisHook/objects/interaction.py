from dataclasses import dataclass, field
from typing import Dict, Optional, Union
from .enums import Locale

@dataclass
class InteractionChoices:
    """
        Represents an interaction choices object.
        - https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure

        Args:
            name (str): The name of the choice.
            value (Union[str, int, float]): The value of the choice.
            name_localizations (Optional[Dict[Locale, str]], optional): The localized names of the choice. Defaults to None.
    """
    name: str
    value: Union[str, int, float]
    name_localizations: Optional[Dict[Locale, str]] = field(default=None)

    def __post_init__(self):
        # Validate the 'name' field
        if not isinstance(self.name, str) or not (1 <= len(self.name) <= 100):
            raise ValueError("The 'name' field must be a string with 1 to 100 characters.")

        if self.name_localizations is not None:
            if not isinstance(self.name_localizations, dict):
                raise ValueError("The 'name_localizations' field must be a dictionary.")
            for locale, localized_name in self.name_localizations.items():
                if not isinstance(locale, Locale):
                    raise ValueError(f"Invalid locale '{locale}' in 'name_localizations'. It must be an instance of Locale enum.")
                if not isinstance(localized_name, str) or not (1 <= len(localized_name) <= 100):
                    raise ValueError(f"All values in 'name_localizations' must be strings with 1 to 100 characters. Error in locale '{locale.value}'.")

        # Validate the 'value' field
        if isinstance(self.value, str):
            if not (1 <= len(self.value) <= 100):
                raise ValueError("The 'value' field must be a string with up to 100 characters.")
        elif not isinstance(self.value, (int, float)):
            raise ValueError("The 'value' field must be a string, integer, or double.")

    def __dict__(self):
        """
            Returns the dictionary representation of the object.

            Returns:
                dict: The dictionary representation of the object.
        """
        return {
            "name": self.name,
            "value": self.value,
            "name_localizations": {locale.value: localized_name for locale, localized_name in self.name_localizations.items()} if self.name_localizations else None
        }
