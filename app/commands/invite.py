from .base import Command


class InviteCommand(Command):
    async def run(self, message: str) -> None:
        # user is not in any voice channel
        if not message.author.voice:
            await message.channel.send("You are not in any voice channel.")
            return

        voice_channel = message.author.voice.channel
        await voice_channel.connect()
