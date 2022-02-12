from src.endpoints.ElixirEndpoint import ElixirEndpoint
from src.Main import Main

class EndpointManager:

    def __init__(self, main: Main, key: str):
        self.elixirEndpoint = ElixirEndpoint()
        self.key = key
        self.main = main

    def getElixirEndpoint(self) -> ElixirEndpoint:
        return self.elixirEndpoint

    def getMainInstance(self):
        return self.main

    def getApiKey(self) -> str:
        return self.key