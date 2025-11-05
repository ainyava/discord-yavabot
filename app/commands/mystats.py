from .base import Command
from app.database.functions import get_users_count


class MyStatsCommand(Command):
    """
    describe to user that how many sound tracks they ha've played!
    """

    async def run(self, message):
        user_name = message.author.name
        count = get_users_count(user_name)
        await message.channel.send(f"You have played {count} many sound tracks.")
