import pytest
from router.cities import Cities


@pytest.fixture(name="df", scope="session", autouse=True)
def fixture_df():
    cities = Cities(["Burlington", "Ottawa", "Montreal"])
    return cities.load()


def test_load(df):
    assert df.index.size == 3
    assert df.columns.size == 3
    assert df.columns[0] == "city"
    assert df.columns[1] == "lat"
    assert df.columns[2] == "lon"


def test_cities_dataframe_calcs_lats(df):
    assert round(rounded_loc(df, "Burlington", "lat"), ndigits=2) == 43.32
    assert round(rounded_loc(df, "Ottawa", "lat"), ndigits=2) == 45.42
    assert round(rounded_loc(df, "Montreal", "lat"), ndigits=2) == 45.50


def test_cities_dataframe_calcs_lons(df):
    assert round(rounded_loc(df, "Burlington", "lon"), ndigits=2) == -79.80
    assert round(rounded_loc(df, "Ottawa", "lon"), ndigits=2) == -75.69
    assert round(rounded_loc(df, "Montreal", "lon"), ndigits=2) == -73.57


def rounded_loc(df, city, coord):
    return float(df[df["city"] == city][coord].iloc[0])
