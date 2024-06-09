# DisHook 🎣

DisHook is a small, lightweight Python package for creating and managing Discord webhook messages easily.

![DisHook Logo](https://github.com/Daftscientist/DisHook/raw/main/assets/logo.png)

## Features ✨

- **Easy Integration**: Simple API for creating and sending Discord webhook messages.
- **Embed Support**: Build rich embed messages with titles, descriptions, fields, and colors.
- **Customization**: Control the appearance of your messages with various options.
- **Lightweight**: Minimalistic design for quick setup and performance.

## Installation 🚀

Install DisHook directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/Daftscientist/DisHook.git
```

## Usage 🛠️

```python
from DisHook import Webhook

webhook = Webhook("https://discord.webhook.url")
webhook.set_content("Hello, world!")

webhook.send()
```

<details>
    <summary>Embed</summary>

```python
from DisHook import Webhook, Embed, EmbedThumbnail

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

<details>
    <summary>Polls</summary>

```python
from DisHook import Webhook, Poll, PartialEmoji, PollMedia, PollAnswer

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
from DisHook import Webhook, AllowedMentions

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
from DisHook import Webhook, ActionRow, Button

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

For more usage examples, check out the [examples](examples) directory.

## Contributing 🤝

Contributions are welcome! Please feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About 👨‍💻

DisHook is a small, lightweight Discord webhook API wrapper created with Python by Daftscientist.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/github/license/Daftscientist/DisHook?style=for-the-badge)
