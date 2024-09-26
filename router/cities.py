"""
Loads coordinates for a list of cities from a remote service.
"""

from time import sleep
import pandas as pd
import geopy
import geopy.geocoders
from geopy.exc import GeocoderTimedOut


class Cities:
    def __init__(self, cities: list[str]):
        self.cities = list(cities)

    def load(self) -> pd.DataFrame:
        geolocator = geopy.geocoders.Nominatim(user_agent="tsp_pandas")
        lats, lons = [], []
        for city in self.cities:
            lat, lon = self.get_lat_lon(geolocator, city)
            lats.append(lat)
            lons.append(lon)
        return pd.DataFrame({"city": self.cities, "lat": lats, "lon": lons})

    def get_lat_lon(self, geolocator, city) -> tuple[float, float]:
        """
        Get the latitude and longitude for the given city.

        Mulitple retries with exponential backoff are used when the service is unavailable.
        """
        MAX_RETRIES = 4
        retries = 0
        while retries < MAX_RETRIES:
            try:
                loc = geolocator.geocode(city, country_codes="ca")
                return (loc.latitude, loc.longitude)
            except GeocoderTimedOut:
                wait_time = 0.5 * ((retries**2) + 1)
                print(f"Timed-out for city {city}, waiting for {wait_time} seconds...")
                retries += 1
                sleep(wait_time)

        raise ConnectionError(f"Unable to get latitude/longitude for {city}")
