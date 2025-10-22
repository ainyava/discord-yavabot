from discord import Client, User
from app.utils import format_command


SOUND_EFFECT_COUNTER = {}


def increment_user_sound_count(user: User):
    if user.name not in SOUND_EFFECT_COUNTER:
        SOUND_EFFECT_COUNTER[user.name] = 1
    else:
        SOUND_EFFECT_COUNTER[user.name] += 1


def register_sound_effect_handler(client: Client):
    @client.event
    async def on_voice_channel_effect(effect):
        increment_user_sound_count(effect.user)
