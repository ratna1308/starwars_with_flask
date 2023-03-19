from resources.films import Film
from resources.characters import Character
from resources.planets import Planet
from resources.species import Species
from resources.starships import Starship
from resources.vehicles import Vehicle
from pprint import pprint
from resources.base import ResourceBase

from utils.fetch_data import hit_url

url = https://swapi.dev/

def __init__(self) -> None:
    super().__init__()
    self.relative_url = "/api/films"

def get_resource_urls(self):
    complete_url = self.home_url + self.relative_url
    response = hit_url(complete_url)
    for u in response:
        return u

if __name__=="__main__":
    pprint(url.get_resource_urls())