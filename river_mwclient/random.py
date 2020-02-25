from .wiki_client import WikiClient
from .gamepedia_client import GamepediaClient
from .cargo_client import CargoClient
from .esports_client import EsportsClient
from .auth_credentials import AuthCredentials


def start_shit(wiki, credentials: AuthCredentials=None, stg=False, **kwargs):
    suffix = 'io' if stg else 'com'
    wiki = EsportsClient.get_wiki(wiki)
    wiki = '{}.gamepedia.{}'.format(wiki, suffix)
    client = WikiClient(wiki, path='/', credentials=credentials, **kwargs)
    cargo_client = CargoClient(client)
    gp_client = GamepediaClient(client=client, cargo_client=cargo_client)
    esp_client = EsportsClient(wiki, gp_client=gp_client)


def start_shit2(wiki, credentials: AuthCredentials=None, stg=False, **kwargs):
    suffix = 'io' if stg else 'com'
    wiki = '{}.gamepedia.{}'.format(wiki, suffix)
    client = WikiClient(wiki, path='/', credentials=credentials, **kwargs)
    cargo_client = CargoClient(client)
    gp_client = GamepediaClient(client=client, cargo_client=cargo_client)
