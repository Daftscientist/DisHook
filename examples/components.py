from DisHook import Webhook, ActionRow, Button

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("This message has an attached action row! It even has a button!")

""" Components will only function if the webhook has been created by an application. Meaning created by a bot."""

my_button = Button(
    label="Click me!",
    style=1,
    custom_id="button1"
)

my_action_row = ActionRow(
    components=[my_button]
)

webhook.add_component(my_action_row)

webhook.send()