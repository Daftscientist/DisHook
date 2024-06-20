from dataclasses import dataclass, field
from typing import Dict, Union, Optional
from .interaction_callback import InteractionCallbackMessage, InteractionCallbackAutocomplete


@dataclass
class InteractionResponse:
    """
        Represents an interaction response object.
    """
    type: int
    data: Union[InteractionCallbackMessage, InteractionCallbackAutocomplete]

    def __post_init__(self):
        if not self.type in [1, 4, 5, 6, 7, 8, 9, 10]:
            raise ValueError("Invalid interaction response type.")

    def __dict__(self):
        return {
            "type": self.type,
            "data": self.data.__dict__()
        }
