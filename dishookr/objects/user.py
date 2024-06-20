from dataclasses import dataclass
from typing import Optional

@dataclass
class AvatarDecorationData:
    asset: str
    sku_id: str

@dataclass
class User():
    """
        Represents a Discord User.
        - https://discord.com/developers/docs/resources/user#user-object

        Args:
            id (str): The ID of the user.
            username (str): The username of the user.
            discriminator (str): The discriminator of the user.
            global_name (Optional[str], optional): The global name of the user. Defaults to None.
            avatar (Optional[str], optional): The avatar hash of the user. Defaults to None.
            bot (Optional[bool], optional): Whether the user is a bot. Defaults to None.
            system (Optional[bool], optional): Whether the user is an Official Discord System user. Defaults to None.
            mfa_enabled (Optional[bool], optional): Whether the user has two-factor authentication enabled. Defaults to None.
            banner (Optional[str], optional): The banner hash of the user. Defaults to None.
            accent_color (Optional[int], optional): The user's accent color. Defaults to None.
            locale (Optional[str], optional): The user's chosen language option. Defaults to None.
            verified (Optional[bool], optional): Whether the user is verified. Defaults to None.
            email (Optional[str], optional): The email of the user. Defaults to None.
            flags (Optional[int], optional): The flags of the user. Defaults to None.
            premium_type (Optional[int], optional): The type of Nitro subscription. Defaults to None.
            public_flags (Optional[int], optional): The public flags of the user. Defaults to None.
            avatar_decoration_data (Optional[AvatarDecorationData], optional): The avatar decoration data of the user. Defaults to None.
    """
    id: str
    username: str
    discriminator: str
    global_name: Optional[str] = None
    avatar: Optional[str] = None
    bot: Optional[bool] = None
    system: Optional[bool] = None
    mfa_enabled: Optional[bool] = None
    banner: Optional[str] = None
    accent_color: Optional[int] = None
    locale: Optional[str] = None
    verified: Optional[bool] = None
    email: Optional[str] = None
    flags: Optional[int] = None
    premium_type: Optional[int] = None
    public_flags: Optional[int] = None
    avatar_decoration_data: Optional[AvatarDecorationData] = None

