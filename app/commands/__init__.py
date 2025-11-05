from .ping import PingCommand
from .invite import InviteCommand
from .mystats import MyStatsCommand


Commands = {
    "ping": PingCommand,
    "test": PingCommand,
    "invite": InviteCommand,
    "mystats": MyStatsCommand,
}
__all__ = [
    "Commands",
]
