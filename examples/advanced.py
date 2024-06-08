from DisHook import Webhook, Embed, EmbedThumbnail, AllowedMentions, Poll, PollMedia, PartialEmoji, ActionRow, Button

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("This message is jam-packed with features! <@1248973121864601694>")

""" Allowed mentions! """
webhook.set_allowed_mentions(
    AllowedMentions(
        users=[1248973121864601694], # Allows the mention to this specific user to take effect
        replied_user=False ## Allows the mention to the replied user to take effect
    )

)

""" Embeds! """
my_embed = Embed(
    title="Embed Title",
    description="This is an embedded message.",
    color=0x00ff00, thumbnail=EmbedThumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
)

my_embed.add_field(name="Field 1", value="Value 1")

webhook.add_embed(my_embed)

""" Polls! """
my_poll = Poll(
    question=PollMedia("What is your favorite color?"),
    duration=3,
    allow_multiselect=False
)

my_poll.add_answer(PollMedia("Red", PartialEmoji(name="🟥")))
my_poll.add_answer(PollMedia("Green", PartialEmoji(name="🟩")))
my_poll.add_answer(PollMedia("Blue", PartialEmoji(name="🟦")))
my_poll.add_answer(PollMedia("Yellow", PartialEmoji(name="🟨")))
my_poll.add_answer(PollMedia("Other", PartialEmoji(name="❓")))

webhook.add_poll(my_poll)

""" Components! """
webhook.add_component(
    ActionRow(
        components=[
            Button(
                style=1,
                label="Click me!",
                custom_id="button1"
            )
        ]
    )
)

webhook.send()