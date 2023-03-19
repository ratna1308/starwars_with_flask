"""
----------------------
PROBLEM STATEMENT
----------------------


The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.

"""


import sys
import random
import argparse

import requests
import json
import pdb

from typing import List
from utils.timing import timeit
from utils.randgen import ProduceChars
from flask import Flask, Response


app = Flask(__name__)

@app.route("/")
def generate_random_numbers(n: int = 15) -> list:
    """produces n random numbers (default 15)"""

    i = 1
    result = []
    while i <= n:
        result.append(random.randint(1, 83))
        i += 1
    return result

@app.route("/get")
def get_url():
    """
    Args:
        resource_id:
    Returns:
    """

    home_url = "https://swapi.dev"
    relative_url = "/api/{}/{}"
    absolute_url = home_url + relative_url.format("films", 1)
    return absolute_url



@app.route("/taskone/<resource>/<int:count>/<int:start>/<int:end>")
def task_one(resource, count, start, end):

    print("[ INFO ]")

    obj = ProduceChars(
        start,
        end,
        count
    )

    resources = [element for element in obj]
    print(f"resources - {resources}")

    print(f"[ INFO ] produced {len(resources)}"
          f" random resource ids in range({start}, {end}).")

    data = []
    for resource_id in resources:
        print(f"[ INFO ] fetching data for resource_id {resource_id}...")
        url_ = get_url(resource_id, resource)

        # `requests.get()` returns a HttpResponse
        res = requests.get(url_)
        print(f"res.status_code = {res.status_code}")

        if res.status_code == 200:
            # getting dict value from response object
            result = res.json()

            # capturing name from dict object
            data.append(result.get("name"))

    output = {
        "count": len(data),
        "names": data
    }

    return Response(json.dumps(output), status=201, mimetype="application/json")

#     print(data)
# #
#
# if __name__ == "__main__":
#     """
#    HOME-URL :: https://swapi.dev
#    relative-URL:: /api/people/1
#
#    URL
#    https://swapi.dev/api/people/1/
#
#    """
#
#     main()