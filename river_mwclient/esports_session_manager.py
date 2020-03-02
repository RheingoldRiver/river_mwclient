from .wiki_client import WikiClient
from .gamepedia_client import GamepediaClient
from .cargo_client import CargoClient
from .esports_client import EsportsClient
from .auth_credentials import AuthCredentials


class EsportsSessionManager(object):
    """Manages instances of EsportsClient
    """
    existing_wikis = {}
    credentials: AuthCredentials = None
    stg: str = False
    login_args = {}

    def __init__(self, credentials: AuthCredentials = None, stg=False, **kwargs):
        self.stg = stg
        self.credentials = credentials
        self.login_args = kwargs

    def get_client(self, wiki):
        if self.existing_wikis[wiki]:
            return self.existing_wikis[wiki]
        suffix = 'io' if self.stg else 'com'
        wiki = EsportsClient.get_wiki(wiki)
        wiki = '{}.gamepedia.{}'.format(wiki, suffix)
        client = WikiClient(wiki, path='/', credentials=self.credentials, **self.login_args)
        cargo_client = CargoClient(client)
        gp_client = GamepediaClient(client=client, cargo_client=cargo_client)
        esp_client = EsportsClient(wiki, gp_client=gp_client)
        return esp_client
