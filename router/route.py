"""
Representation of a particular route across multiple cities.

Primarily for yielding formatted output of a route's distance and cities.
"""


class Route:
    def __init__(self, distance: float, route: list[str]):
        self.distance = distance
        self.route = list(route)

    def __str__(self):
        distance = round(self.distance, ndigits=2)
        return f"Distance: {distance} miles\nRoute:{self.route}"
