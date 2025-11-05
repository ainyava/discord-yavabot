from discord import Client
from app.config import settings
from app.commands import Commands


def register_message_handler(client: Client):
    @client.event
    async def on_message(message):
        # ignore irrelavant messages
        if not message.content.startswith(settings.COMMAND_PREFIX):
            return

        command_message = message.content[len(settings.COMMAND_PREFIX) :]
        if command_message not in Commands.keys():
            print(f"Command: {command_message} not found")
            return

        # invoke the relavant command
        print(f"Command: {command_message} from {message.author}: `{message.content}`")
        command = Commands[command_message]()
        await command.run(message=message)
