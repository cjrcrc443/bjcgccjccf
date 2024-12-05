import os

from AlinaXIQ.utils.decorators import asyncify
from config import autoclean


@asyncify
def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except Exception:
                    pass
    except Exception:
        pass
