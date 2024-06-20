from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    # Define the structure of the User object if needed
    id: str
    username: str
    discriminator: str
    avatar: Optional[str] = None

@dataclass
class PartialGuild:
    # Define the structure of the Partial Guild object if needed
    id: str
    name: str

@dataclass
class PartialChannel:
    # Define the structure of the Partial Channel object if needed
    id: str
    name: str

@dataclass
class Webhook:
    id: str
    type: int[1, 2, 3]
    guild_id: Optional[str] = None
    channel_id: Optional[str] = None
    user: Optional[User] = None
    name: Optional[str] = None
    avatar: Optional[str] = None
    token: Optional[str] = None
    application_id: Optional[str] = None
    source_guild: Optional[PartialGuild] = None
    source_channel: Optional[PartialChannel] = None
    url: Optional[str] = None

# Example usage
if __name__ == "__main__":
    user = User(id="123", username="testuser", discriminator="0001")
    webhook = Webhook(
        id="456",
        type=1,
        guild_id="789",
        channel_id="012",
        user=user,
        name="Test Webhook",
        avatar=None,
        token="securetoken",
        application_id="345",
        source_guild=None,
        source_channel=None,
        url="https://example.com/webhook"
    )
    print(webhook)
