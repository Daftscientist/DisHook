import DisHook
from DisHook import embed

webhook = DisHook.App(
    "https://discord.com/api/webhooks/939504960041799721/fvLR-DRPKTxC2RuUTPWxV9kbo3sF4rjbWpY211wnwqftQR0nz3MiwsgINHwy-glhC3vb",
    default_username="sus",
    default_avatar_url=""
)


myEmbed = embed.Generate(description=f"**🏓 |** Current Ping: 279.91ms")

webhook.webby.test()