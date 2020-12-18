from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str] = []

    def valid_extension(self,extension):
        return extension is in self.extensions

    def parser(path: Path,source: Path,dest: Path):
        raise NotImplementedError

    def read (path):
        with open(path, 'r') as file:
            return file.read

    def write(path,dest,content,ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open (full_path, 'w' ) as file:
            file.write(content)

    def copy (path,source,dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extension = [".jpg", ".png", ".gif", ".css", ".html"]

    def parser(path: Path, source: Path, dest: Path):
        super.copy2(path,source,dest)
