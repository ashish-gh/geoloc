from __future__ import annotations

import copy
import json
import os
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Dict, List

import numpy as np
from loguru import logger


@dataclass
class Location(metaclass=ABCMeta):
    """ """

    city: str = None
    region: str = None
    country: str = None
    latitude: float = None
    longitude: float = None
    timezone: str = None

    def get_current_location(self) -> Location:
        pass
        # return Location(
        #     city=
        # )

    def filter_by_lat_long(self):
        """
        Filter location based on latitude and longitude
        """
        raise NotImplementedError

    @staticmethod
    def filter_lat_long(current_lat, current_long, lat, lon):
        res = (
            np.arccos(
                np.sin(current_lat) * np.sin(lat)
                + np.cos(current_lat) * np.cos(lat) * np.cos(lon - current_long)
            )
            * 6371
        )
        return res


def main():
    pass
    # res = [funct(lat, lon, d['lat'], d['lon']) for d in all_data]


if __name__ == "__main__":
    main()
    # location_tracker = CurlLocationFetcher()
    # data= location_tracker.get_location()
    # if data:
    #     print(data)
    #     lat_long = data.get('loc','').split(',')
    #     print(f"Lat : {lat_long[0]} | Long : {lat_long[1]}")
