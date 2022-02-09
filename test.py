import DisHook 

webhook = DisHook.App(
    "https://discord.com/api/webhooks/",
    default_username="isa is gay",
    default_avatar_url=""
)


myWebhook = webhook.send(content="Hello! I am a webhook!")
## Sending the initial webhook.

print(webhook.get(myWebhook.id).content)
## Fetching the webhook
webhook.edit(myWebhook.id, content="Bye! I am an edited webhook")
## Editing the webhook
print(webhook.get(myWebhook.id).content)
## Fetching the webhook
webhook.delete(myWebhook.id)
## Deleting the webhook

## This will be updated to work like myWebhook.edit and myWebhook.delete later.