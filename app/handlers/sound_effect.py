from discord import Client, VoiceChannelEffect
from app.database.functions import add_sound_track_play
from datetime import datetime

SOUND_EFFECT_COUNTER = {}


def increment_user_sound_count(effect: VoiceChannelEffect):
    add_sound_track_play(
        username=effect.user.name,
        played_at=datetime.now(),
        sound_track=effect.emoji.name,
    )


def register_sound_effect_handler(client: Client):
    @client.event
    async def on_voice_channel_effect(effect):
        increment_user_sound_count(effect)
