from os import getenv
from dotenv import load_dotenv
load_dotenv()

class Config:

    def __init__(self): pass

    def get(self, key: str) -> str:
        """
        @param key: The key to obtain from the config.
        @type key: str
        @return: The value pair.
        @rtype: str
        """
        return getenv(key)