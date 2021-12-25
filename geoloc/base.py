from abc import ABCMeta, abstractmethod


class Fetcher(metaclass=ABCMeta):
    """
    Base class from which we derive all the fetching of location, coordinates

    Possible Implementation
        - CurlLocationFetcher
    """

    @abstractmethod
    def fetch(self, **kwargs):
        pass

    @property
    def __clasname__(self) -> str:
        return self.__class__.__name__


def main():
    pass


if __name__ == "__main__":
    main()
