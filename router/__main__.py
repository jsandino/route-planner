#!/usr/bin/env python
"""
Optimal Route Calculator
"""
import click
import pandas as pd

from router.cities import Cities
from router.route import Route
from router.timed import timed
from router.tsp import find_shortest_route

sample_cities = [
    "Toronto",
    "Montreal",
    "Ottawa",
    "Mississauga",
    "Brampton",
    "Hamilton",
    "Quebec City",
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


def main(count, show, save):
    df = cities_dataframe()
    save_cities(df, save)
    shortest, route = get_shortest_route(df, count, show)
    print("\n" + "=" * 50)
    print("Shortest route found:")
    print(f"{Route(shortest, route)}")
    print("=" * 50)
    # print(df.head())


def save_cities(df: pd.DataFrame, save: bool):
    if save:
        df.to_csv("data/cities.csv")


@timed
def cities_dataframe(cities: list[str] = None) -> pd.DataFrame:
    cities = cities or sample_cities
    df = Cities(cities).load()
    return df


@timed
def get_shortest_route(df, n, s) -> tuple[float, list[str]]:
    return find_shortest_route(df, n, s)


@click.group
def commands():
    """Command Line Tool to calculate the shortest distance across multiple cities."""


@commands.command("run")
@click.option("--count", default=10, help="Total number of times to calculate a route.")
@click.option(
    "--show", is_flag=True, default=False, help="Show route calculation output."
)
@click.option(
    "--save", is_flag=True, default=False, help="Save cities data frame to csv file."
)
def run(count, show, save):
    """
    Run the route calculator multiple times for a number of random routes.

    Example: ./main.py run --count 10
    """
    print(f"Running route calculator {count} times")
    main(count, show, save)


if __name__ == "__main__":
    commands()
