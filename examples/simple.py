from dishook import Webhook

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("Hello, world!")

webhook.send()
