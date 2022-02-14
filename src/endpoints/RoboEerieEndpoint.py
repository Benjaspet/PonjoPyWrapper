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

class RoboEerieEndpoint:

    def __init__(self, key: str, uri: str):
        self.key = key
        self.uri = uri

    def getRoboEerieTags(self, count: int = 5) -> object:

        """
        @param count: The amount of tags to fetch.
        @type count: int
        @return: JSON response
        @rtype: object
        """

        response: Response = RequestFactory(self.key)\
            .setURL(f'{self.uri}?count={count}')\
            .setHeaders({"Authorization": self.key})\
            .setMethod("GET")\
            .build()

        try:
            response.raise_for_status()
            return response.json()
        except HTTPError:
            return response.json()