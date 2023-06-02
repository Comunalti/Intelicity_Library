from pathlib import Path

from andre import *

class Container:

    def __init__(self,contents: list[FileContent]):
        self.contents = contents
        pass

    def save(self, path: Path) -> None:
        with open(path, 'w') as file:
            for file_content in self.contents:
                file.write(str(file_content))
