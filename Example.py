from src.Wrapper import PonjoPyWrapper
from src.endpoints.ElixirEndpoint import ElixirEndpoint

ponjoApi: PonjoPyWrapper = PonjoPyWrapper("YOUR-API-KEY")

# Get tne endpoint you'd like to use:

elixirEndpoint: ElixirEndpoint = ponjoApi.getEndpointManager().getElixirEndpoint()

# Finally, you can use the endpoint to get the data you want:

print(elixirEndpoint.getNowPlayingTrack("828296827882831913"))