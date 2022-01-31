import DisHook 
from DisHook import embed

webhook = DisHook.App("https://discord.com/api/webhooks/925455555802300467/thZBietLUMcTusvleDX_D805i8JaamF8dh_Y7UanxecA2EcttzULKi4f_K_rlfE2H12F")

embed = embed.Generate(
    title="hello"
)

result = webhook.send()
print(result.json())