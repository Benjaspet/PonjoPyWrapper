import requests
from requests import HTTPError
from src.Main import Main

class ElixirEndpoint:

    def __init__(self): pass

    def getNowPlayingTrack(self, guild: str) -> object:
        """
        @param guild: The guild ID of the music queue.
        @type guild: str
        @return: JSON response
        @rtype: object
        """
        headers = {"Authorization": Main().key}
        result = requests.get(f'https://app.ponjo.club/v1/elixir/nowplaying?guild={guild}', headers=headers)
        try:
            result.raise_for_status()
            return result.json()
        except HTTPError:
            return result.json()