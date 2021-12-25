import math
from dataclasses import dataclass
from typing import Dict

from .coordiante import Coordinate


class GeoLocation(Coordinate):
    """
    Class representing a coordinate on a sphere, most likely Earth.

    For full implementation look at.
    ....

    """

    MIN_LAT = math.radians(-90)
    MAX_LAT = math.radians(90)
    MIN_LON = math.radians(-180)
    MAX_LON = math.radians(180)
    EARTH_RADIUS = 6378.1  # kilometers

    def to_radians(self, deg_lat: float = None, deg_lon: float = None) -> None:
        """
        Convert degree into radians
        Args:
            `deg_lat`: float
            `deg_lon`: float
        """
        rad_lat = math.radians(deg_lat)
        rad_lon = math.radians(deg_lon)
        return rad_lat, rad_lon

    def __init__(self, deg_lat: float = None, deg_lon: float = None) -> None:
        if not isinstance(deg_lat, (int, float)):
            raise TypeError(
                f"Expected value to be type (float, int). Got : {type(str(deg_lat))}"
            )
        if not isinstance(deg_lon, (int, float)):
            raise TypeError(
                f"Expected value to be type (float, int). Got : {type(str(deg_lon))}"
            )
        self.deg_lat = float(deg_lat)
        self.deg_lon = float(deg_lon)
        self.rad_lat, self.rad_lon = self.to_radians(self.deg_lat, self.deg_lon)
        self._check_bounds()

    def _check_bounds(self):
        if (
            self.rad_lat < GeoLocation.MIN_LAT
            or self.rad_lat > GeoLocation.MAX_LAT
            or self.rad_lon < GeoLocation.MIN_LON
            or self.rad_lon > GeoLocation.MAX_LON
        ):
            raise Exception(
                f"Illegal arguments : Unwanted parameters either in Latitude: {self.rad_lat } or Longitude {self.rad_lon}"
            )

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def distance_to(
        self, coordinate: Coordinate = None, radius: int = EARTH_RADIUS
    ) -> Dict:
        """
        Computes the great circle distance between this GeoLocation instance
        and the other.
        TODO:
        - represent other in form of coordiantes as other is also a coordiante
        """
        if not isinstance(coordinate, Coordinate):
            raise TypeError(
                f"Expected type to be class.Coordinates. Got type : {str(type(coordinate))}"
            )
        return radius * math.acos(
            math.sin(self.rad_lat) * math.sin(coordinate.rad_lat)
            + math.cos(self.rad_lat)
            * math.cos(coordinate.rad_lat)
            * math.cos(self.rad_lon - coordinate.rad_lon)
        )

    def bounding_locations(self, distance, radius=EARTH_RADIUS):
        """
        Computes the bounding coordinates of all points on the surface
        of a sphere that has a great circle distance to the point represented
        by this GeoLocation instance that is less or equal to the distance argument.

        Param:
            distance - the distance from the point represented by this GeoLocation
                       instance. Must be measured in the same unit as the radius
                       argument (which is kilometers by default)

            radius   - the radius of the sphere. defaults to Earth's radius.

        Returns a list of two GeoLoations - the SW corner and the NE corner - that
        represents the bounding box.
        """

        if radius < 0 or distance < 0:
            raise Exception("Illegal arguments")

        # angular distance in radians on a great circle
        rad_dist = distance / radius

        min_lat = self.rad_lat - rad_dist
        max_lat = self.rad_lat + rad_dist

        if min_lat > GeoLocation.MIN_LAT and max_lat < GeoLocation.MAX_LAT:
            delta_lon = math.asin(math.sin(rad_dist) / math.cos(self.rad_lat))

            min_lon = self.rad_lon - delta_lon
            if min_lon < GeoLocation.MIN_LON:
                min_lon += 2 * math.pi

            max_lon = self.rad_lon + delta_lon
            if max_lon > GeoLocation.MAX_LON:
                max_lon -= 2 * math.pi
        # a pole is within the distance
        else:
            min_lat = max(min_lat, GeoLocation.MIN_LAT)
            max_lat = min(max_lat, GeoLocation.MAX_LAT)
            min_lon = GeoLocation.MIN_LON
            max_lon = GeoLocation.MAX_LON

        return [
            GeoLocation.from_radians(min_lat, min_lon),
            GeoLocation.from_radians(max_lat, max_lon),
        ]


def main():
    pass


if __name__ == "__main__":
    main()
