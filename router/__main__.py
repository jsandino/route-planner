#!/usr/bin/env python
"""
Optimal Route Calculator
"""
import click
import pandas as pd

from router.cities import Cities
from router.route import Route
from router.tsp import find_shortest_route

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


def main(n, s):
    df = cities_dataframe()
    shortest, route = find_shortest_route(df, n, s)
    print("\n" + "=" * 50)
    print("Shortest route found:")
    print(f"{Route(shortest, route)}")
    print("=" * 50)
    # print(df.head())


def cities_dataframe(cities: list[str] = None) -> pd.DataFrame:
    cities = cities or sample_cities
    return Cities(cities).load()


@click.group
def commands():
    """Command Line Tool to calculate the shortest distance across multiple cities."""


@commands.command("run")
@click.option("-n", default=10, help="Total number of times to calculate a route.")
@click.option("-s", is_flag=True, default=False, help="Show route calculation output.")
def run(n, s):
    """
    Run the route calculator n number of times.

    Example: ./main.py run -n 10
    """
    print(f"Running route calculator {n} times")
    main(n, s)


if __name__ == "__main__":
    commands()
