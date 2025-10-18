from discord import Client
from app.utils import format_command


def register_message_handler(client: Client):
    @client.event
    async def on_message(message):
        if message.content.startswith(format_command("ping")):
            channel = message.channel
            await channel.send("pong!")
