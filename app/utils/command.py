from app.config import settings


def format_command(command: str) -> str:
    return f"{settings.COMMAND_PREFIX}{command}"
