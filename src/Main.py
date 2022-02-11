import sys
from src.utils.StartupUtil import StartupUtil
import src.Constants as Constants

class Main:

    def __init__(self):
        self.key = Constants.API_KEY
        if not StartupUtil().isApiKeyValid():
            print("An invalid API key was provided. Please obtain one by emailing benpetrillo@ponjo.club.")
            sys.exit(0)