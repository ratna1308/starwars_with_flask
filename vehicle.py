import json
import requests
from pprint import pprint
from typing import Dict, List

FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


def write_data_into_file(data: Dict, filename: str) -> None:
    """writes dict data into a file"""
    with open(filename, "w") as fp:
        fp.write(json.dumps(data))


def get_movie_data() -> Dict:
    """Returns a dict object for the first Star Wars movie"""
    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_, "output.txt")
    return result_


def get_character_names(data_: Dict) -> List:
    """Returns a list of character names in the movie"""
    characters = data_.get("characters")
    names = []
    for char_url in characters:
        char_data = requests.get(char_url).json()
        names.append(char_data.get("name"))
    return names


def get_planet_names(data_: Dict) -> List:
    """Returns a list of planet names in the movie"""
    planets = data_.get("planets")
    names = []
    for planet_url in planets:
        planet_data = requests.get(planet_url).json()
        names.append(planet_data.get("name"))
    return names


def get_vehicle_names(data_: Dict) -> List:
    """Returns a list of vehicle names in the movie"""
    vehicles = data_.get("vehicles")
    names = []
    for vehicle_url in vehicles:
        vehicle_data = requests.get(vehicle_url).json()
        names.append(vehicle_data.get("name"))
    return names


if __name__ == "__main__":
    # retrieve movie data
    movie_data = get_movie_data()
    pprint(movie_data)

    # retrieve character names
    character_names = get_character_names(movie_data)
    pprint(character_names)

    # retrieve planet names
    planet_names = get_planet_names(movie_data)
    pprint(planet_names)

    # retrieve vehicle names
    vehicle_names = get_vehicle_names(movie_data)
    pprint(vehicle_names)
