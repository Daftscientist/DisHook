from dishook import Emoji

"""
- This is an example of how to use the Emoji class to create an emoji object that is fully accepted by Discord.
- This Emoji object is not to be confused with PartialEmoji, which is used in PollMedia objects.
"""

emoji = Emoji(name="🎉")

print(emoji.to_dict())
