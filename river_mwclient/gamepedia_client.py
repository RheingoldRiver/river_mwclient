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

    def __init__(self, wiki: str=None, stg=False,
                 client: WikiClient = None, cargo_client: CargoClient = None,
                 username=None, password=None, user_file=None,
                 **kwargs):
        if client:
            self.client = client
        else:
            suffix = 'io' if stg else 'com'
            wiki = '%s.gamepedia.' % wiki + suffix
            self.client = WikiClient(wiki, path='/',
                                     username=username, password=password, user_file=user_file,
                                     **kwargs)
        if cargo_client:
            self.cargo_client = cargo_client
        else:
            self.cargo_client = CargoClient(client=self.client)
