# PonjoPyWrapper

A wrapper for the Ponjo API written in Python.

- Note: this library required Python `3.10` or later to run properly, as it uses function return type specification and variable typing.

## Documentation

#### Initializing the Wrapper

Before using the wrapper, you'll need to obtain an API key for the Ponjo API.
You can view more information about the API [on its website](https://app.ponjo.club).

Next, make sure to install all library requirements:

```shell
pip3 install -r requirements.txt
```

Next, you'll have to initialize the wrapper in order to use it:

```python
from src.Wrapper import PonjoPyWrapper
from src.endpoints.ElixirEndpoint import ElixirEndpoint

ponjoApi: PonjoPyWrapper = PonjoPyWrapper("YOUR-API-KEY")

# Get tne endpoint you'd like to use:

elixirEndpoint: ElixirEndpoint = ponjoApi.getEndpointManager().getElixirEndpoint()

# Finally, you can use the endpoint to get the data you want:

print(elixirEndpoint.getNowPlayingTrack("828296827882831913"))
```