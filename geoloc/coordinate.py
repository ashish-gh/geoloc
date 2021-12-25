from dataclasses import dataclass


@dataclass
class Coordinate:
    """
    Represents current latitude and longitude on map.
    Properties: list if have any
    """

    # TODO
    # - add setter and getter both

    current_latitude: float = None
    current_longitude: float = None

    def is_valid_coordinate(self):
        """
        Check values of latitude and longitude.
        """
        ...

    def get_current_coordiante(self) -> Coordinate:
        return Coordinate(
            current_latitude=self.current_latitude,
            current_longitude=self.current_longitude,
        )

    def copy(self) -> Coordinate:
        return Coordinate(
            current_latitude=self.current_latitude,
            current_longitude=self.current_longitude,
        )
