from .base import Command


class PingCommand(Command):
    async def run(self, message: str) -> None:
        await message.channel.send("pong!")
