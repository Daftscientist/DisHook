from typing import Optional, List
from datetime import datetime

class EmbedFooter(object):
    """
    Represents the footer of an embed message.
    - https://discord.com/developers/docs/resources/channel#embed-object-embed-footer-structure
    """

    text: str
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]

    def __init__(self, 
                 text: str,
                 icon_url: Optional[str] = None,
                 proxy_icon_url: Optional[str] = None):
        """
        Initializes a new instance of the EmbedFooter class.

        Args:
            text (str): The text of the footer.
            icon_url (Optional[str], optional): The URL of the footer icon. Defaults to None.
            proxy_icon_url (Optional[str], optional): The proxy URL of the footer icon. Defaults to None.
        """
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url
    
    def __dict__(self):
        """
        Returns a dictionary representation of the EmbedFooter object.

        Returns:
            dict: A dictionary representation of the EmbedFooter object.
        """
        return {
            'text': self.text,
            'icon_url': self.icon_url,
            'proxy_icon_url': self.proxy_icon_url
        }

class EmbedImage(object):
    """
    Represents an image in an embed.
    - https://discord.com/developers/docs/resources/channel#embed-object-embed-image-structure
    """

    def __init__(self, 
                 url: str,
                 proxy_url: Optional[str] = None,
                 height: Optional[int] = None,
                 width: Optional[int] = None):
        """
            Initializes a new instance of the EmbedImage class.
            
            Args:
                url (str): The URL of the image.
                proxy_url (Optional[str], optional): The proxy URL of the image. Defaults to None.
                height (Optional[int], optional): The height of the image. Defaults to None.
                width (Optional[int], optional): The width of the image. Defaults to None.
        """
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width
    
    def __dict__(self):
        """
            Returns a dictionary representation of the EmbedImage object.

            Returns:
                dict: A dictionary containing the attributes of the EmbedImage object.
        """
        return {
            'url': self.url,
            'proxy_url': self.proxy_url,
            'height': self.height,
            'width': self.width
        }

class EmbedThumbnail(object):
    """
        Represents the thumbnail of an embed.
        - https://discord.com/developers/docs/resources/channel#embed-object-embed-thumbnail-structure
    """
    url: str
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]

    def __init__(self, 
                 url: str,
                 proxy_url: Optional[str] = None,
                 height: Optional[int] = None,
                 width: Optional[int] = None):
        """
            Initializes a new instance of the EmbedThumbnail class.

            Args:
                url (str): The URL of the thumbnail.
                proxy_url (Optional[str], optional): The proxy URL of the thumbnail. Defaults to None.
                height (Optional[int], optional): The height of the thumbnail. Defaults to None.
                width (Optional[int], optional): The width of the thumbnail. Defaults to None.
            
        """
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width
    
    def __dict__(self):
        """
            Returns a dictionary representation of the EmbedThumbnail object.

            Returns:
                dict: A dictionary containing the attributes of the EmbedThumbnail object.
        """
        return {
            'url': self.url,
            'proxy_url': self.proxy_url,
            'height': self.height,
            'width': self.width
        }

class EmbedVideo(object):
    """
    Represents an embedded video.
    - https://discord.com/developers/docs/resources/channel#embed-object-embed-video-structure
    """

    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]

    def __init__(self, 
                 url: Optional[str] = None,
                 proxy_url: Optional[str] = None,
                 height: Optional[int] = None,
                 width: Optional[int] = None):
        """
        Initializes a new instance of the EmbedVideo class.

        Args:
            url (Optional[str]): The URL of the video.
            proxy_url (Optional[str]): The proxy URL of the video.
            height (Optional[int]): The height of the video.
            width (Optional[int]): The width of the video.
        """
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width
    
    def __dict__(self):
        """
        Returns a dictionary representation of the EmbedVideo object.

        Returns:
            dict: A dictionary containing the attributes of the EmbedVideo object.
        """
        return {
            'url': self.url,
            'proxy_url': self.proxy_url,
            'height': self.height,
            'width': self.width
        }

class EmbedProvider(object):
    """
    Represents the provider of an embed.
    - https://discord.com/developers/docs/resources/channel#embed-object-embed-provider-structure
    """

    name: Optional[str]
    url: Optional[str]

    def __init__(self, 
                 name: Optional[str] = None,
                 url: Optional[str] = None) -> None:
        """
        Initializes a new instance of the EmbedProvider class.

        Args:
            name (Optional[str]): The name of the provider.
            url (Optional[str]): The URL of the provider.
        """
        self.name = name
        self.url = url
    
    def __dict__(self) -> dict:
        """
        Returns a dictionary representation of the EmbedProvider object.

        Returns:
            dict: A dictionary representation of the EmbedProvider object.
        """
        return {
            'name': self.name,
            'url': self.url
        }

class EmbedAuthor(object):
    """
    Represents the author of an embed.
    - https://discord.com/developers/docs/resources/channel#embed-object-embed-author-structure
    """

    name: str
    url: Optional[str]
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]

    def __init__(self, 
                 name: str,
                 url: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 proxy_icon_url: Optional[str] = None):
        """
        Initializes a new instance of the EmbedAuthor class.

        Args:
            name (str): The name of the author.
            url (Optional[str], optional): The URL of the author. Defaults to None.
            icon_url (Optional[str], optional): The URL of the author's icon. Defaults to None.
            proxy_icon_url (Optional[str], optional): The proxy URL of the author's icon. Defaults to None.
        """
        self.name = name
        self.url = url
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    def __dict__(self):
        """
        Returns a dictionary representation of the EmbedAuthor object.

        Returns:
            dict: A dictionary representation of the EmbedAuthor object.
        """
        return {
            'name': self.name,
            'url': self.url,
            'icon_url': self.icon_url,
            'proxy_icon_url': self.proxy_icon_url
        }

class EmbedField(object):
    """
    Represents a field in an embed message.
    - https://discord.com/developers/docs/resources/channel#embed-object-embed-field-structure
    """

    name: str
    value: str
    inline: Optional[bool]

    def __init__(self, 
                 name: str,
                 value: str,
                 inline: Optional[bool] = False) -> None:
        """
        Initializes a new instance of the EmbedField class.

        Args:
            name (str): The name of the field.
            value (str): The value of the field.
            inline (bool, optional): Whether the field should be displayed inline. Defaults to False.
        """
        self.name = name
        self.value = value
        self.inline = inline
    
    def __dict__(self) -> dict:
        """
        Returns a dictionary representation of the EmbedField object.

        Returns:
            dict: A dictionary representation of the EmbedField object.
        """
        return {
            'name': self.name,
            'value': self.value,
            'inline': self.inline
        }

class Embed(object):
    """
    Represents an embed message.
    - https://discord.com/developers/docs/resources/channel#embed-object
    """
    title: Optional[str]
    type: Optional[str] = "rich"
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[datetime]
    color: Optional[int]
    footer: Optional[EmbedFooter]
    image: Optional[EmbedImage]
    thumbnail: Optional[EmbedThumbnail]
    video: Optional[EmbedVideo]
    provider: Optional[EmbedProvider]
    author: Optional[EmbedAuthor]
    fields: Optional[List[EmbedField]]

    def __init__(self, 
                 title: Optional[str] = None,
                 type: str = "rich",
                 description: Optional[str] = None,
                 url: Optional[str] = None,
                 timestamp: Optional[datetime] = None,
                 color: Optional[int] = None,
                 footer: Optional[EmbedFooter] = None,
                 image: Optional[EmbedImage] = None,
                 thumbnail: Optional[EmbedThumbnail] = None,
                 video: Optional[EmbedVideo] = None,
                 provider: Optional[EmbedProvider] = None,
                 author: Optional[EmbedAuthor] = None,
                 fields: Optional[List[EmbedField]] = None) -> None:
        """
        Initializes a new instance of the Embed class.

        Args:
            title (str, optional): The title of the embed. Defaults to None.
            type (str, optional): The type of the embed. Defaults to "rich".
            description (str, optional): The description of the embed. Defaults to None.
            url (str, optional): The URL of the embed. Defaults to None.
            timestamp (datetime, optional): The timestamp of the embed. Defaults to None.
            color (int, optional): The color of the embed. Defaults to None.
            footer (EmbedFooter, optional): The footer of the embed. Defaults to None.
            image (EmbedImage, optional): The image of the embed. Defaults to None.
            thumbnail (EmbedThumbnail, optional): The thumbnail of the embed. Defaults to None.
            video (EmbedVideo, optional): The video of the embed. Defaults to None.
            provider (EmbedProvider, optional): The provider of the embed. Defaults to None.
            author (EmbedAuthor, optional): The author of the embed. Defaults to None.
            fields (List[EmbedField], optional): The fields of the embed. Defaults to None.
        
        Raises:
            ValueError: If any of the embed limits are exceeded.
        """
        self.title = title
        self.type = type
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.thumbnail = thumbnail
        self.video = video
        self.provider = provider
        self.author = author
        self.fields = fields if fields is not None else []

        self.validate()

    def validate(self) -> None:
            """
            Validates the embed object based on Discord's embed limits.

            Raises:
                ValueError: If any of the embed limits are exceeded.
            """
            if self.title and len(self.title) > 256:
                raise ValueError("Title cannot exceed 256 characters.")
            if self.description and len(self.description) > 4096:
                raise ValueError("Description cannot exceed 4096 characters.")
            if len(self.fields) > 25:
                raise ValueError("Cannot have more than 25 fields.")
            if self.footer and self.footer.text and len(self.footer.text) > 2048:
                raise ValueError("Footer text cannot exceed 2048 characters.")
            if self.author and self.author.name and len(self.author.name) > 256:
                raise ValueError("Author name cannot exceed 256 characters.")
            
            total_chars = (len(self.title or "") + len(self.description or "") +
                           sum(len(field.name) for field in self.fields) +
                           sum(len(field.value) for field in self.fields) +
                           (len(self.footer.text) if self.footer and self.footer.text else 0) +
                           (len(self.author.name) if self.author and self.author.name else 0))
            
            if total_chars > 6000:
                raise ValueError("Combined characters in title, description, fields, footer text, and author name cannot exceed 6000.")

    def add_field(self, name: str, value: str, inline: Optional[bool] = None) -> None:
        """
        Adds a field to the embed.

        Args:
            name (str): The name of the field.
            value (str): The value of the field.
            inline (bool, optional): Whether the field should be displayed inline. Defaults to None.

        Raises:
            ValueError: If the maximum number of fields (25) has been reached.
        """
        if len(self.fields) < 25:
            self.fields.append(
                EmbedField(name=name, value=value, inline=inline)
            )
            self.validate()
        else:
            raise ValueError("Maximum of 25 fields are allowed.")
    
    def __dict__(self) -> dict:
        """
        Returns a dictionary representation of the Embed object.

        Returns:
            dict: A dictionary containing the attributes of the Embed object.
        """
        return {
            'title': self.title,
            'type': self.type,
            'description': self.description,
            'url': self.url,
            'timestamp': self.timestamp,
            'color': self.color,
            'footer': self.footer.__dict__() if self.footer is not None else None,
            'image': self.image.__dict__() if self.image is not None else None,
            'thumbnail': self.thumbnail.__dict__() if self.thumbnail is not None else None,
            'video': self.video.__dict__() if self.video is not None else None,
            'provider': self.provider.__dict__() if self.provider is not None else None,
            'author': self.author.__dict__() if self.author is not None else None,
            'fields': [field.__dict__() for field in self.fields]
        }
