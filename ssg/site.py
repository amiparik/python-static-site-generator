from pathlib import Path

class Site():
    def __init__(self,source, dest):
        self.source = Path (source)
        self.dest =  Path (dest)

    def creat_dir(self,path):
        directory = self.dest + "/" + path.relative_to(self.source)
        directory.mkdir(True,True)

    def build():
        self.dest.mkdir(True,True)
        for path in self.source.rglob("*"):
            if path.isdir():
                creat_dir(path)
                
