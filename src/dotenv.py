import configparser
from pathlib import Path


class DotEnv:
    def __init__(self, source: Path | None = None) -> None:
        self.parser = configparser.ConfigParser()
        self.parser.read((source or Path("")) / ".env")

    def __getattr__(self, __section: str):
        return type("Section", (), dict(self.parser.items(__section)))()
