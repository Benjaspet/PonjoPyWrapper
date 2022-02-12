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

import requests
from src.exceptions.WrapperExceptions import InvalidRequestParameterException

class RequestFactory:

    url = None
    method = None
    headers = None
    timeout = None

    def __init__(self, key: str):
        self.key = key

    @classmethod
    def setURL(cls, url: str):
        cls.url = url
        return cls

    @classmethod
    def setMethod(cls, method: str):
        cls.method = method
        return cls

    @classmethod
    def setHeaders(cls, headers: dict):
        cls.headers = headers
        return cls

    @classmethod
    def setTimeout(cls, timeout: int):
        cls.timeout = timeout
        return cls

    @classmethod
    def build(cls) -> requests or Exception:
        if not cls.url or not cls.method or not cls.headers:
            raise InvalidRequestParameterException("Missing one of required methods: setURL(), setMethod(), setHeaders().")
        if cls.method == "GET":
            if not cls.timeout:
                return requests.get(cls.url, headers=cls.headers)
            else:
                return requests.get(cls.url, headers=cls.headers, timeout=cls.timeout)