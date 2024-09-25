import pytest

from main import sample_cities
from main import cities_dataframe


def test_sample_cities():
    assert len(sample_cities) > 10
    assert "Burlington" in sample_cities
    assert "Toronto" in sample_cities
    assert "Ottawa" in sample_cities


df = cities_dataframe()


def test_cities_dataframe():
    assert df.index.size == len(sample_cities)
    assert df.columns.size == 3
    assert df.columns[0] == "city"
    assert df.columns[1] == "lat"
    assert df.columns[2] == "lon"


def test_cities_dataframe_calcs_lats():
    assert round(rounded_loc("Burlington", "lat"), ndigits=2) == 43.32
    assert round(rounded_loc("Ottawa", "lat"), ndigits=2) == 45.42
    assert round(rounded_loc("Montreal", "lat"), ndigits=2) == 45.50


def test_cities_dataframe_calcs_lons():
    assert round(rounded_loc("Burlington", "lon"), ndigits=2) == -79.80
    assert round(rounded_loc("Ottawa", "lon"), ndigits=2) == -75.69
    assert round(rounded_loc("Montreal", "lon"), ndigits=2) == -73.57


def rounded_loc(city, coord):
    return float(df[df["city"] == city][coord].iloc[0])
