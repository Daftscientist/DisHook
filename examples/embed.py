from DisHook import Webhook, Embed, EmbedThumbnail

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("This message has an attached embed!")

my_embed = Embed(
    title="Embed Title",
    description="This is an embedded message.",
    color=0x00ff00, thumbnail=EmbedThumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
)

my_embed.add_field(name="Field 1", value="Value 1")

webhook.add_embed(my_embed)

webhook.send()