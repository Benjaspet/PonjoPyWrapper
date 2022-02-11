import requests
from src.Config import Config

class StartupUtil:

    def __init__(self): pass

    # Determine if the provided API key in the config is valid.
    # @return bool

    def isApiKeyValid(self) -> bool:
        result = requests.get("https://app.ponjo.club/v1/covid", headers={"Authorization": Config().get("API-KEY")})
        if result.status_code == 403:
            return False
        return True