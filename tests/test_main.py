from router.__main__ import sample_cities
from router.__main__ import cities_dataframe


def test_sample_cities():
    assert len(sample_cities) > 10
    assert "Burlington" in sample_cities
    assert "Toronto" in sample_cities
    assert "Ottawa" in sample_cities


def test_cities_dataframe():
    df = cities_dataframe(["Toronto", "Ottawa"])
    assert df.index.size == 2
    assert df.columns.size == 3
    assert df.columns[0] == "city"
    assert df.columns[1] == "lat"
    assert df.columns[2] == "lon"
