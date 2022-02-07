import DisHook 
from DisHook import embed, helpers

webhook = DisHook.App(
    "https://discord.com/api/webhooks/939948451360292894/ii-uwpM3qYHfckbDLuvxBaRQDbRcIVPBIOmAjer8QClhnJVU_kT74daEcsp90WP2jTH1",
    default_username="",
    default_avatar_url=""
)


result = webhook.send(content="`@everyone`", embeds=[embed.Generate(description="wumpus dumb")])
print(result)