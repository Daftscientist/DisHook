import DisHook 
from DisHook import embed

webhook = DisHook.App(
    "https://discord.com/api/webhooks/936912274218713118/VT_627xIESpVbvdN2OqkM0EIPfm9z2Dt8N5dK5nneh44zQfEiQUZ7XhI98X-zYps2HjB",
    default_username="",
    default_avatar_url=""
)

myField = embed.Field(name="hi", value="lol")

embed = embed.Generate(
    title="hello",
    description="hiiiii",
    fields=[myField]
)

print(embed.title)

result = webhook.send(content="raw message", embeds=[embed])
print(result.json())