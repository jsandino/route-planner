"""
A Heuristic solution to the Traveling Salesman Problem.

The general idea is to:
    1. randomly generate a route configuration across all cities
    2. calculate the distance for the given route
    3. record the calculated distance
    4. repeat steps 1 to 3 many times
    5. select the shortes calculated distance among all calculations
"""

from random import shuffle
from geopy import distance as gdist
import pandas as pd

from router.route import Route


def find_shortest_route(
    cities_df: pd.DataFrame, n: int, show_all: bool = False
) -> tuple[float, list[str]]:
    """
    Calculates the distance between cities for n random route configurations.

    The shortest distance, along with the associated route is returned.

    Parameters:
        cities_df: DataFrame of cities ("city", "lat", "lon")
        n: number of times that a random route distance should be calculated

    Returns:
        The shortest distance, along with the associated route.
    """
    routes = dict()
    for _ in range(n):
        distance, route = random_route_distance(cities_df)
        routes[distance] = route

    shortest = min(routes.keys())

    show_routes(routes, show_all)

    return shortest, routes[shortest]


def show_routes(routes: dict[float : list[str]], show: bool):
    """
    Shows all route calculations to standard out.
    """

    if show:
        print()
        for distance, route in routes.items():
            print(f"{Route(distance, route)}\n")


def random_route_distance(cities_df: pd.DataFrame) -> tuple[float, list[str]]:
    """
    Calculates the distance across a given (randomly generated) route
    """
    cities = cities_df["city"].to_list()
    shuffle(cities)
    return calculate_route(cities, cities_df)


def calculate_route(cities: list[str], df: pd.DataFrame) -> tuple[float, list[str]]:
    """
    Calculates the total distance to visit each city in the supplied list.
    """
    distances = []  # distances between each of the cities

    for i in range(len(cities) - 1):
        # Calculate distances for all cities, from first to last
        distances.append(calc_distance(cities[i], cities[i + 1], df))

    # Calculate distance from last city to first, to close the loop
    distances.append(calc_distance(cities[-1], cities[0], df))

    total_distance = sum(distances)

    return total_distance, cities


def calc_distance(source, destination, df) -> float:
    from_city = lat_lon_for(source, df)
    to_city = lat_lon_for(destination, df)
    return gdist.distance(from_city, to_city).miles


def lat_lon_for(city: str, df: pd.DataFrame) -> tuple[float, float]:
    lat = df[df["city"] == city]["lat"].values[0]
    lon = df[df["city"] == city]["lon"].values[0]
    return lat, lon
