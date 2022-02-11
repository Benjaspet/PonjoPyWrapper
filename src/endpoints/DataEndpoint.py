from src.Config import Config

class DataEndpoint:

    def __init__(self):
        self.key = Config().get("API-KEY")

    def getApiKey(self):
        if not self.key: return None
        return self.key