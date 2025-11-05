GET_USERS_SOUND_TRACK_COUNT = """
SELECT count(*) as total_count FROM sound_track_ledger
WHERE username=?;
"""
