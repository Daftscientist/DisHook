from DisHook import Webhook, Embed, EmbedAuthor, Poll, PollMedia, PartialEmoji, AllowedMentions, ActionRow, Button

my_hook = Webhook("", wait=True)

my_hook.set_content("Hello, world! <@491630879085559808>")

my_hook.set_allowed_mentions(
    AllowedMentions(
        parse=["roles"],
        users=[491630879085559808],
        replied_user=True
    )
)

my_hook.add_component(
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

my_hook.send()
