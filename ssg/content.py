import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter,re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = __regex.split(string,2)
        load(fm, Loader=FullLoader)
        return cls(metadata,content)

    def __init__(self, metadata, content):
        self.data = Metadata
        self.content = {"content": self.data}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"]

    @type.setter
    def type(self, type):
        self.data["type"] = type


    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        return str(data)

    def __str__(self):
