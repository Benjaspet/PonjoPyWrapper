from os import getenv
from dotenv import load_dotenv
load_dotenv()

class Config:

    def __init__(self): pass

    def get(self, key: str) -> str:
        return getenv(key)