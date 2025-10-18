import discord
from app.config import settings
from app.handlers import register_message_handler


class YavaDiscordClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

# build app and its handlers
client = YavaDiscordClient(
    intents=intents,
    proxy=settings.PROXY,
)
register_message_handler(client)


client.run(token=settings.DISCORD_TOKEN)
