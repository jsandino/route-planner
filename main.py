#!/usr/bin/env python
"""
Optimal Route Calculator
"""
import click

sample_cities = [
    "Toronto",
    "Montreal",
    "Calgary",
    "Ottawa",
    "Edmonton",
    "Winnipeg",
    "Mississauga",
    "Vancouver",
    "Brampton",
    "Hamilton",
    "Surrey",
    "Quebec City",
    "Halifax",
    "Laval",
    "London",
    "Markham",
    "Vaughan",
    "Gatineau",
    "Saskatoon",
    "Kitchener",
    "Longueuil",
    "Burnaby",
    "Windsor",
    "Regina",
    "Oakvile",
    "Richmond",
    "Richmond Hill",
    "Burlington",
]


def main(n):
    print(n)


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
