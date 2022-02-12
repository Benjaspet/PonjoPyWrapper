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

import sys
from src.utils.StartupUtil import StartupUtil
from src.managers.EndpointManager import EndpointManager

class PonjoPyWrapper:

    endpointManager = None

    def __init__(self, key: str):
        self.key = key
        self.endpointManager = EndpointManager(self.key)
        if not StartupUtil(self.key).isApiKeyValid():
            print("An invalid API key was provided. Please obtain one by emailing benpetrillo@ponjo.club.")
            sys.exit(0)

    def getEndpointManager(self):
        return self.endpointManager