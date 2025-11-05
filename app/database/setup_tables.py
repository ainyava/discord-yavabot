from sqlite3 import Connection
from .queries.sound_tracks import SOUND_TRACKS_TABLE_QUERY


def setup_tables(connection: Connection) -> None:
    # setup sound tracks table
    cursor = connection.cursor()
    cursor.execute(SOUND_TRACKS_TABLE_QUERY)
    connection.commit()
