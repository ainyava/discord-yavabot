from discord import Client
from app.utils import format_command
from app.config import settings
from app.handlers.sound_effect import SOUND_EFFECT_COUNTER


def register_message_handler(client: Client):
    @client.event
    async def on_message(message):
        channel = message.channel
        if message.content.startswith(settings.COMMAND_PREFIX):
            print(f"Message from {message.author}: {message.content}")

        if message.content.startswith(format_command("ping")):
            await channel.send("pong!")

        # invite bot to voice channels
        if message.content == format_command("invite"):
            # user is not in any voice channel
            if not message.author.voice:
                await channel.send("You are not in any voice channel.")
                return

            voice_channel = message.author.voice.channel
            await voice_channel.connect()

        # describe to user that how many sound tracks they ha've played!
        if message.content == format_command("mystats"):
            user_name = message.author.name
            if user_name not in SOUND_EFFECT_COUNTER:
                count = 0
            else:
                count = SOUND_EFFECT_COUNTER[user_name]
            await channel.send(f"You have played {count} many sound tracks.")
