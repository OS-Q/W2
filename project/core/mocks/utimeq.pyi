from typing import *

class utimeq:
    def __init__(self, max_queue_size: int) -> None: ...
    def push(self, time: int, callback: Any, value: Any) -> None: ...
    def pop(self, entry: List[Any]) -> None: ...
    def peektime(self) -> int: ...
    def discard(self, callback: Any) -> None: ...
