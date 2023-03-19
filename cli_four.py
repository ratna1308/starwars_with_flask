"""
The task 2 goes like following:
Pull data for the the first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import json
import requests
import argparse


from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url, fetch_data

FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("four.txt", "w") as fp:
        fp.write(json.dumps(data))


def first_task (url: str, output_filename: str) -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""

    response = requests.get(url)
    result_ = response.json()
    write_data_into_file(result_)
    return result_


def second_task(film_data: Dict) -> List:
    """pull data from swapi characters sequentially"""

    characters = film_data.get("characters")  # returns None by default

    names = []
    for character in characters:
        character_data = hit_url(character)
        character_data = character_data.json()
        names.append(character_data.get("name"))

    # names = []
    # all_characters = fetch_data(characters)
    # for character in all_characters:
    #     names.append(character.get("name"))

    return names


def third_task(film_data: Dict) -> List:
    """pull data from swapi planets sequentially"""

    planets = film_data.get("planets")  # returns None by default

    names = []
    for planet in planets:
        planet_data = hit_url(planet)
        planet_data = planet_data.json()
        names.append(planet_data.get("name"))

    return names


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The project on swapi.API,converted into command line application")
    parser.add_argument("task", choices=["first","second","third"], help="task choosed by user")
    parser.add_argument("--url", default="https://swapi.dev/api/films/1/",help="please enter url from swapi.dev")
    parser.add_argument("--output",default="four.txt",help="output printed")
    args = parser.parse_args()

    if args.task == "first":
        result = first_task(args.url, args.output)
        pprint(result)

    elif args.task == "second":
        result = first_task(args.url, args.output)
        names = second_task(result)
        pprint(names)

    elif args.task == "third":
        result = first_task(args.url, args.output)
        planets = third_task(result)
        pprint(planets)
