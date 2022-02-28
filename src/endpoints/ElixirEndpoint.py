"""
Copyright 2022 Ben Petrillo. All rights reserved.

Project licensed under the MIT License: https://www.mit.edu/~amini/LICENSE.md

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

All portions of this software are available for public use, provided that
credit is given to the original author(s).
"""

from requests import HTTPError, Response
from src.http.RequestFactory import RequestFactory

class ElixirEndpoint:

    def __init__(self, key: str):
        self.key = key

    async def getNowPlayingTrack(self, guild: str, bot: str) -> object:

        """
        @param bot: The Elixir bot ID.
        @param guild: The guild ID of the music queue.
        @return: JSON response
        @rtype: object
        """

        response: Response = RequestFactory(self.key)\
            .setURL(f'https://app.ponjo.club/v1/elixir/nowplaying?guild={guild}&bot={bot}')\
            .setHeaders({"Authorization": self.key})\
            .setMethod("GET")\
            .build()

        try:
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            return response.json()

    async def getCustomPlaylistById(self, playlistId: str) -> object:

        """
        @param playlistId: The ID of the custom playlist.
        @type playlistId: str
        @return: JSON response
        @rtype: object
        """

        response: Response = RequestFactory(self.key)\
            .setURL(f'https://app.ponjo.club/v1/elixir/playlist/fetch?id={playlistId}')\
            .setHeaders({"Authorization": self.key})\
            .setMethod("GET")\
            .build()

        try:
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            return response.json()

    async def getGuildMusicQueueById(self, guild: str, bot: str):

        """
        @param guild: The guild ID of the music guild.
        @param bot: The Elixir bot ID.
        @return: JSON response
        @rtype: object
        """

        response: Response = RequestFactory(self.key)\
            .setURL(f'https://app.ponjo.club/v1/elixir/queue?guild={guild}&bot={bot}')\
            .setHeaders({"Authorizations": self.key})\
            .setMethod("GET")\
            .build()

        try:
            response.raise_for_status()
            return response.json()
        except HTTPError as err:
            return response.json()