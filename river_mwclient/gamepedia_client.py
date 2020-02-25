from .wiki_client import WikiClient
from .cargo_client import CargoClient


class GamepediaClient(object):
    """
    Functions for connecting to and editing Gamepedia wikis. As with ExtendedSite, the focus of support
    is Gamepedia esports wikis specifically, but no functions here require using an esports wiki to work.

    Cargo-specific functions should be in CargoSite
    """
    cargo_client = None
    client = None

    def __init__(self, client: WikiClient = None, cargo_client: CargoClient = None, **kwargs):
        self.client = client
        self.cargo_client = cargo_client
