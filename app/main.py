import discord
from app.config import settings
from app.handlers import register_message_handler, register_sound_effect_handler


class YavaDiscordClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")


intents = discord.Intents.default()
intents.message_content = True

# build app and its handlers
client = YavaDiscordClient(
    intents=intents,
    proxy=settings.PROXY,
)
register_message_handler(client)
register_sound_effect_handler(client)


client.run(token=settings.DISCORD_TOKEN)
