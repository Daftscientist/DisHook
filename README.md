# DisHook

DisHook is a Python package for creating and managing Discord webhook messages easily.

## Installation

You can install DisHook using pip:

```
pip install DisHook
```

## Usage

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

## Features

- **Easy Integration:** Simple API for creating and sending Discord webhook messages.
- **Embed Support:** Build rich embed messages with titles, descriptions, fields, and colors.
- **Customization:** Control the appearance of your messages with various options.
- **Lightweight:** Minimalistic design for quick setup and performance.

## Examples

Check out the [examples](https://github.com/Daftscientist/DisHook/tree/main/examples) directory for more usage examples.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Daftscientist/DisHook/blob/main/LICENSE) file for details.
