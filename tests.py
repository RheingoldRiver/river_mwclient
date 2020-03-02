from river_mwclient.esports_client import EsportsClient

site = EsportsClient('lol')

print(site.client.pages['Faker'])
