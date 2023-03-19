from resources.r_films import RFilms

from models.datamodels.films import Films
from models.datamodels.planets import Planets
from models.datamodels.species import Species
from models.datamodels.starships import Starships
from models.datamodels.characters import Characters
from models.datamodels.vehicles import Vehicles


from dal.db_conn_helper import conn_toml
from dal.dml import insert_resource
from utils.fetch_data import hit_url
from utils.time import timeit


def store_characters_data():
    characters = film_data.characters
    char_columns = ["name",
                    "height",
                    "mass",
                    "hair_color",
                    "skin_color",
                    "eye_color",
                    "birth_year",
                    "gender",
                    "homeworld",
                    "created",
                    "edited",
                    "url"
                    ]
    for char in characters:
        response = hit_url(char)
        char_data = response.json()
        char_data = Characters(**char_data)
        char_values = [char_data.name,
                       char_data.height,
                       char_data.mass,
                       char_data.hair_color,
                       char_data.skin_color,
                       char_data.eye_color,
                       char_data.birth_year,
                       char_data.gender,
                       char_data.homeworld,
                       char_data.created.strftime("%y-%m-%d"),
                       char_data.edited.strftime("%y-%m-%d"),
                       char_data.url
                       ]
        char_id = int(char_data.url.split("/")[-2])
        insert_resource("characters",
                        "char_id",
                        char_id,
                        char_columns,
                        char_values)


def store_planets_data():
    planets = film_data.planets
    planet_columns = ["name",
                      "rotation_period",
                      "orbital_period",
                      "diameter",
                      "climate",
                      "gravity",
                      "terrain",
                      "surface_water",
                      "population",
                      "created",
                      "edited",
                      "url"
                      ]

    for planet in planets:
        response = hit_url(planet)
        planet_data = response.json()
        planet_data = Planets(**planet_data)
        planet_values = [planet_data.name,
                         planet_data.rotation_period,
                         planet_data.orbital_period,
                         planet_data.diameter,
                         planet_data.climate,
                         planet_data.gravity,
                         planet_data.terrain,
                         planet_data.surface_water,
                         planet_data.population,
                         planet_data.created.strftime("%y-%m-%d"),
                         planet_data.edited.strftime("%y-%m-%d"),
                         planet_data.url
                         ]

        planet_id = int(planet_data.url.split("/")[-2])
        insert_resource("planet",
                        "planet_id",
                        planet_id,
                        planet_columns,
                        planet_values)


def store_vehicles_data():
    vehicles = film_data.vehicles
    vehicle_columns = ["name",
                       "model",
                       "manufacturer",
                       "cost_in_credits",
                       "length",
                       "max_atmosphering_speed",
                       "crew",
                       "passengers",
                       "cargo_capacity",
                       "consumables",
                       "vehicle_class",
                       "created",
                       "edited",
                       "url"
                       ]

    for vehicle in vehicles:
        response = hit_url(vehicle)
        vehicle_data = response.json()
        vehicle_data = Vehicles(**vehicle_data)
        vehicle_values = [vehicle_data.name,
                          vehicle_data.model,
                          vehicle_data.manufacturer,
                          vehicle_data.cost_in_credits,
                          vehicle_data.length,
                          vehicle_data.max_atmosphering_speed,
                          vehicle_data.crew,
                          vehicle_data.passengers,
                          vehicle_data.cargo_capacity,
                          vehicle_data.consumables,
                          vehicle_data.vehicle_class,
                          vehicle_data.created.strftime("%y-%m-%d"),
                          vehicle_data.edited.strftime("%y-%m-%d"),
                          vehicle_data.url
                          ]

        vehicle_id = int(vehicle_data.url.split("/")[-2])

        insert_resource("vehicle",
                        "vehicle_id",
                        vehicle_id,
                        vehicle_columns,
                        vehicle_values)


def store_starships_data():
    starships = film_data.starships
    starship_columns = ["name",
                        "model",
                        "manufacturer",
                        "cost_in_credits",
                        "length",
                        "max_atmosphering_speed",
                        "crew",
                        "passengers",
                        "cargo_capacity",
                        "consumables",
                        "hyperdrive_rating",
                        "MGLT",
                        "starship_class",
                        "created",
                        "edited",
                        "url"
                        ]

    for starship in starships:
        response = hit_url(starship)
        starship_data = response.json()
        starship_data = Starships(**starship_data)
        starship_values = [starship_data.name,
                           starship_data.model,
                           starship_data.manufacturer,
                           starship_data.cost_in_credits,
                           starship_data.length,
                           starship_data.max_atmosphering_speed,
                           starship_data.crew,
                           starship_data.passengers,
                           starship_data.cargo_capacity,
                           starship_data.consumables,
                           starship_data.hyperdrive_rating,
                           starship_data.MGLT,
                           starship_data.starship_class,
                           starship_data.created.strftime("%y-%m-%d"),
                           starship_data.edited.strftime("%y-%m-%d"),
                           starship_data.url
                           ]

        starship_id = int(starship_data.url.split("/")[-2])

        insert_resource("starship",
                        "starship_id",
                        starship_id,
                        starship_columns,
                        starship_values)


def store_species_data():
    species = film_data.species
    specie_columns = ["name",
                      "classification",
                      "designation",
                      "average_height",
                      "skin_colors",
                      "hair_colors",
                      "eye_colors",
                      "average_lifespan",
                      "homeworld",
                      "language",
                      "created",
                      "edited",
                      "url"
                      ]

    for specie in species:
        response = hit_url(specie)
        specie_data = response.json()
        specie_data = Species(**specie_data)
        specie_values = [specie_data.name,
                         specie_data.classification,
                         specie_data.designation,
                         specie_data.average_height,
                         specie_data.skin_colors,
                         specie_data.hair_colors,
                         specie_data.eye_colors,
                         specie_data.average_lifespan,
                         specie_data.homeworld,
                         specie_data.language,
                         specie_data.created.strftime("%y-%m-%d"),
                         specie_data.edited.strftime("%y-%m-%d"),
                         specie_data.url
                         ]

        specie_id = int(specie_data.url.split("/")[-2])

        insert_resource("species",
                        "species_id",
                        specie_id,
                        specie_columns,
                        specie_values)


@timeit
def main():
    store_characters_data()
    store_planets_data()
    store_vehicles_data()
    store_starships_data()
    store_species_data()


if __name__ == "__main__":
    film_obj = RFilms()
    film_ = film_obj.get_sample_data(id_=1)
    film_data = Films(**film_)

    # establishing the connection
    conn = conn_toml()

    film_columns = ["title",
                    "episode_id",
                    "opening_crawl",
                    "director",
                    "producer",
                    "release_date",
                    "created",
                    "edited",
                    "url",
                    ]
    film_values = [film_data.title,
                   film_data.episode_id,
                   film_data.opening_crawl,
                   film_data.director,
                   film_data.producer,
                   film_data.release_date,
                   film_data.created.strftime("%y-%m-%d"),
                   film_data.edited.strftime("%y-%m-%d"),
                   film_data.url
                   ]
    film_id = int(film_data.url.split("/")[-2])
    result = insert_resource("film",
                             "film_id",
                             film_id,
                             film_columns,
                             film_values)
    main()
