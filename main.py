#!/usr/bin/env python
"""
Optimal Route Calculator
"""
from time import sleep
import click
import pandas as pd
import geopy
import geopy.geocoders
from geopy.exc import GeocoderTimedOut

sample_cities = [
    "Toronto",
    "Montreal",
    "Ottawa",
    "Mississauga",
    "Brampton",
    "Hamilton",
    "Quebec City",
    "Halifax",
    "Laval",
    "London",
    "Markham",
    "Vaughan",
    "Kitchener",
    "Windsor",
    "Oakville",
    "Richmond Hill",
    "Burlington",
]


def main(n):
    print(n)
    # df = cities_dataframe()
    # print(df.head())


def cities_dataframe() -> pd.DataFrame:
    geolocator = geopy.geocoders.Nominatim(user_agent="tsp_pandas")
    cities = sample_cities.copy()
    lats = []
    lons = []
    for city in cities:
        lat, lon = get_lat_lon(geolocator, city)
        lats.append(lat)
        lons.append(lon)
    return pd.DataFrame({"city": cities, "lat": lats, "lon": lons})


def get_lat_lon(geolocator, city) -> tuple[float, float]:
    """
    Get the latitude and longitude for the given city.

    Mulitple retries with exponential backoff are used when the service is unavailable.
    """
    MAX_RETRIES = 4
    retries = 0
    while retries < MAX_RETRIES:
        try:
            loc = geolocator.geocode(city, country_codes="ca")
            return (loc.latitude, loc.longitude)
        except GeocoderTimedOut:
            wait_time = 0.5 * ((retries**2) + 1)
            print(f"Timed-out for city {city}, waiting for {wait_time} seconds...")
            retries += 1
            sleep(wait_time)

    raise ConnectionError(f"Unable to get latitude/longitude for {city}")


@click.group
def commands():
    """Command Line Tool to calculate the shortest distance across multiple cities."""


@commands.command("run")
@click.option("-n", default=10, help="Total number of times to calculate a route.")
def run(n):
    """
    Run the route calculator n number of times.

    Example: ./main.py run -n 10
    """
    print(f"Running route calculator {n} times")
    main(n)


if __name__ == "__main__":
    commands()
