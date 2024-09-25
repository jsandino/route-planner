#!/usr/bin/env python
"""
Optimal Route Calculator
"""
import click
import geopy.geocoders
import pandas as pd
import geopy

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


def cities_dataframe() -> pd.DataFrame:
    geolocator = geopy.geocoders.Nominatim(user_agent="tsp_pandas")
    cities = sample_cities.copy()
    lats = []
    lons = []
    for city in cities:
        loc = geolocator.geocode(city, country_codes="ca")
        lats.append(loc.latitude)
        lons.append(loc.longitude)
        print(f"City '{city}': lat: {loc.latitude}, lon: {loc.longitude}")
    return pd.DataFrame({"city": cities, "lat": lats, "lon": lons})


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
