from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get(key: str) -> str:
    return getenv(key)