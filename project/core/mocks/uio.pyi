class FileIO: ...

class StringIO:
    def __init__(self, _: Union[int, str]) -> None: ...

class BytesIO:
    def __init__(self, _: Union[int, bytes]) -> None: ...
    def getvalue(self) -> bytes: ...

def open(name: str, mode: str = ...) -> FileIO:
    pass
