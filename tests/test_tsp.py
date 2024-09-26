import pandas as pd
import pytest

from router.tsp import (
    calc_distance,
    calculate_route,
    find_shortest_route,
    random_route_distance,
)


DEFAULT_ROUTE = ["Toronto", "Ottawa", "Montreal"]


@pytest.fixture(name="df")
def fixture_df():
    return pd.DataFrame(
        {
            "city": DEFAULT_ROUTE,
            "lat": [43.653482, 45.420878, 45.503182],
            "lon": [-79.383935, -75.690111, -73.569806],
        }
    )


@pytest.fixture(name="df2")
def fixture_df2():
    return pd.DataFrame(
        {
            "city": ["Mississauga", "Brampton"],
            "lat": [43.589623, 43.685832],
            "lon": [-79.644388, -79.759937],
        }
    )


def test_calc_distance(df):
    assert 314 == round(calc_distance("Toronto", "Montreal", df))


def test_calculate_route(df):
    total_distance, route = calculate_route(DEFAULT_ROUTE, df)
    assert 637 == round(total_distance)
    assert DEFAULT_ROUTE == route


def test_random_route_distance(df):
    passed = False
    for _ in range(5):
        _, route = random_route_distance(df)
        if route != DEFAULT_ROUTE:
            passed = True
            break

    if not passed:
        pytest.fail("Route not randomly generated")


def test_find_shortest_route(df, df2):
    cities_df = pd.concat([df, df2], ignore_index=True)
    distance, _ = find_shortest_route(cities_df, 50)
    assert 674 == round(distance)
