from .wiki_client import WikiClient
from .gamepedia_client import GamepediaClient
from .cargo_client import CargoClient
from .esports_client import EsportsClient
from .auth_credentials import AuthCredentials


class EsportsSessionManager(object):
    """Manages instances of EsportsClient
    """
    existing_wikis = {}

    def get_client(self, wiki: str = None, client: WikiClient = None,
                   credentials: AuthCredentials = None, stg: bool = False,
                   **kwargs):
        if client:
            return client, CargoClient(client)
        suffix = 'io' if stg else 'com'
        wiki = EsportsClient.get_wiki(wiki)
        url = '{}.gamepedia.{}'.format(wiki, suffix)
        if self.existing_wikis[url]:
            return self.existing_wikis[wiki]['client'], self.existing_wikis[wiki]['cargo_client']
        client = WikiClient(url, path='/', credentials=credentials, **kwargs)
        cargo_client = CargoClient(client)
        self.existing_wikis[url] = {'client': client, 'cargo_client': cargo_client}
        return client, cargo_client