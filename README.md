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

### Simple Example

```python
from DisHook import Webhook, Embed

# Initialize webhook
webhook = Webhook(url='your_webhook_url_here')

# Create an embed object
embed = Embed(
    title='Embed Title',
    description='Embed Description',
    color=0xFF5733
)

# Add fields to the embed
embed.add_field(name='Field 1', value='Value 1')
embed.add_field(name='Field 2', value='Value 2')

# Send the embed to the webhook
webhook.send(embed)
```

<details>
    <summary>#### More Examples</summary>
```python
    python
```

</details>

For more usage examples, check out the [examples](examples) directory.

## Contributing 🤝

Contributions are welcome! Please feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About 👨‍💻

DisHook is a small, lightweight Discord webhook API wrapper created with Python by Daftscientist.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/github/license/Daftscientist/DisHook?style=for-the-badge)
