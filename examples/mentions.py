from dishook import Webhook, AllowedMentions

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("Lets test out the mentions system! <@1248973121864601694>")


webhook.set_allowed_mentions(
    AllowedMentions(
        users=[1248973121864601694], # Allows the mention to this specific user to take effect
        replied_user=False ## Allows the mention to the replied user to take effect
    )
)


webhook.send()
