from enum import Enum
import os

HEARTBEAT_DURATION = 30
ELECTION_DURATION = 30


class Role(Enum):
    FOLLOWER = 0,
    CANDIDATE = 1,
    LEADER = 2


SELF_UUID = os.environ.get("URL_0")
NEIGHBOURS = [
    {
        "id": os.environ.get("URL_1"),
        "url": os.environ.get("URL_1")
    },
    {
        "id": os.environ.get("URL_2"),
        "url": os.environ.get("URL_2")
    },
]
