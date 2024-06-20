# DisHook 🎣

DisHook is a small, lightweight Python package for creating and managing Discord webhook messages easily.

## Features ✨

- **User-Friendly Integration**: Simple API for creating and sending Discord webhook messages.
- **Rich Embed Support**: Build visually appealing messages with titles, descriptions, fields, and colors.
- **Polling Functionality**: Conduct polls with various options and durations.
- **Interactive Components**: Add buttons and other interactive elements to webhook messages.
- **Efficient Design**: Minimalistic approach ensures quick setup and optimal performance.

## Installation 🚀

Install DisHook directly from the GitHub repository using pip:

```bash
pip install dishookr
```

## Usage 🛠️

```python
from dishookr import Webhook

webhook = Webhook("https://discord.webhook.url")
webhook.set_content("Hello, world!")

webhook.send()
```

<details>
    <summary>Embed</summary>

```python
from dishookr import Webhook, Embed, EmbedThumbnail

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("This message has an attached embed!")

my_embed = Embed(
    title="Embed Title",
    description="This is an embedded message.",
    color=0x00ff00,
    thumbnail=EmbedThumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
)

my_embed.add_field(name="Field 1", value="Value 1")

webhook.add_embed(my_embed)

webhook.send()
```

</details>

---

<details open>
    <summary>Polls</summary>

```python
from dishookr import Webhook, Poll, PartialEmoji, PollMedia, PollAnswer

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("A poll is attached!")

my_poll = Poll(
    question=PollMedia("What is your favorite color?"),
    duration=3,
    allow_multiselect=False,
)

my_poll.add_answer(PollMedia("Red", PartialEmoji(name="🟥")))
my_poll.add_answer(PollMedia("Green", PartialEmoji(name="🟩")))
my_poll.add_answer(PollMedia("Blue", PartialEmoji(name="🟦")))
my_poll.add_answer(PollMedia("Yellow", PartialEmoji(name="🟨")))
my_poll.add_answer(PollMedia("Other", PartialEmoji(name="❓")))
my_poll.add_answer(PollMedia("I don't know", PartialEmoji(name="🤷")))

webhook.add_poll(my_poll)

webhook.send()
```

</details>

---

<details>
    <summary>Mentions</summary>

```python
from dishookr import Webhook, AllowedMentions

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("Lets test out the mentions system! <@1248973121864601694>")

webhook.set_allowed_mentions(
    AllowedMentions(
        users=[1248973121864601694], # Allows the mention to this specific user to take effect
        replied_user=False # Allows the mention to the replied user to take effect
    )
)

webhook.send()
```

</details>

---

<details>
    <summary>Components</summary>

```python
from dishookr import Webhook, ActionRow, Button

webhook = Webhook("https://discord.webhook.url")

webhook.set_content("This message has an attached action row! It even has a button!")

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
```

</details>

---

<details>
    <summary>Interaction Responses</summary>

```python
from vortexkit import App, Request, JSONResponse
from dishookr import InteractionResponse, InteractionCallbackMessage, InteractionResponseType

app = App()

@app.route("/interaction-callback")
def interaction_callback(request: Request):
    if not request.method == "POST":
        return JSONResponse({"error": "Method not allowed"}, status_code=405)
    
    if not request.body["type"] == 3 and not request.body["data"]["custom_id"] == "button1":
        return JSONResponse({"error": "Invalid interaction type"}, status_code=400)
    
    my_dishook_response = InteractionResponse(
        type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=InteractionCallbackMessage(
            content="You clicked the button!"
        )
    )

    return JSONResponse(
        my_dishook_response.__dict__()
    )


if __name == '__main__':
    app.run("0.0.0.0", 8080)
```

</details>

---

For more usage examples, check out the [examples](examples) directory.

## Contributing 🤝

Contributions are welcome! Please feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About 👨‍💻

DisHook is a small, lightweight Discord webhook API wrapper created with Python by Daftscientist.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/github/license/Daftscientist/DisHook?style=for-the-badge)
