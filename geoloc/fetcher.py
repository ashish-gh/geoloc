import json
import os
from abc import abstractmethod
from typing import Dict

from loguru import logger

from . import Fetcher
from .location import Location


class LocationFetcher(Fetcher, Location):
    @abstractmethod
    def get_address(self):
        """ """
        raise NotImplementedError()


class CurlLocationFetcher(LocationFetcher):
    def fetch(self) -> Dict:
        logger.info("Fetching address using curl fetcher.")
        try:
            raw_data = os.popen("curl ipinfo.io").read()
            if not isinstance(raw_data, str):
                return self._no_location()
            return self.mapper(json.loads(raw_data))
        except Exception as e:
            logger.error(f"Exception in parsing location using curl. Error : {str(e)}")
            return self._no_location()

    def _no_location(self) -> Location:
        """
        Returns empty location
        """
        return Location(
            city="", region="", country="", latitude=None, longitude=None, timezone=""
        )

    def mapper(self, data: Dict = None) -> Location:
        """
        Maps to relavent data structure
        """
        if not data or not isinstance(data, dict):
            return self._no_location()

        lat_long = data.get("loc")
        if lat_long:
            lat_long = lat_long.split(",")
        return Location(
            city=data.get("city", ""),
            region=data.get("region", ""),
            country=data.get("country", ""),
            latitude=lat_long[0] if lat_long else None,
            longitude=lat_long[1] if lat_long else None,
            timezone=data.get("timezone", ""),
        )

    def get_address(self) -> Location:
        """
        Fetch current address.
        Returns
            Args:
            `Location`: instance of class.Location
        """
        data = self.fetch()
        if not data:
            return self._no_location()
        return self.mapper(data)
