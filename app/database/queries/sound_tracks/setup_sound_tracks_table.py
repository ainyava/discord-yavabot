SOUND_TRACKS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS sound_track_ledger (
    id INTEGER PRIMARY KEY,
    username text NOT NULL, 
    played_at DATETIME,
    sound_effect text NOT NULL
);
"""
