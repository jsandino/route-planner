#!/usr/bin/env python
"""
Optimal Route Calculator
"""
import click
import pandas as pd

from router.cities import Cities

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
    df = cities_dataframe()
    print(df.head())


def cities_dataframe(cities: list[str] = None) -> pd.DataFrame:
    cities = cities or sample_cities
    return Cities(cities).load()


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
