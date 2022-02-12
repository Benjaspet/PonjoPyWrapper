from src.Main import Main
from Config import Config

# Creating a new instance of the wrapper.

wrapper = Main(Config().get("API-KEY"))
print(wrapper.getEndpointManager().getElixirEndpoint().getNowPlayingTrack())