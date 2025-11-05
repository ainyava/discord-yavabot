from app.database.queries.sound_tracks import (
    INSERT_SOUND_TRACK_PLAY,
    GET_USERS_SOUND_TRACK_COUNT,
)
from datetime import datetime
from app.database import connection


def add_sound_track_play(
    username: str,
    played_at: datetime,
    sound_track: str,
) -> None:
    cursor = connection.cursor()
    cursor.execute(
        INSERT_SOUND_TRACK_PLAY,
        (
            username,
            played_at,
            sound_track,
        ),
    )
    connection.commit()


def get_users_count(username: str) -> int:
    cursor = connection.cursor()
    cursor.execute(
        GET_USERS_SOUND_TRACK_COUNT,
        (username,),
    )
    return cursor.fetchone()[0]
