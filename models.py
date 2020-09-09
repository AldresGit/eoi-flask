from dataclasses import dataclass

@dataclass
class User:
    username: str

@dataclass
class Post:
    title: str
    text: str