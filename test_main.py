from main import sample_cities


def test_sample_cities():
    assert len(sample_cities) > 10
    assert "Burlington" in sample_cities
    assert "Toronto" in sample_cities
    assert "Ottawa" in sample_cities
