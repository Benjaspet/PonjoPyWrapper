import requests

class StartupUtil:

    def __init__(self, key: str):
        self.key = key

    def isApiKeyValid(self) -> bool:
        result = requests.get("https://app.ponjo.club/v1/covid", headers={"Authorization": self.key})
        if result.status_code == 403:
            return False
        return True