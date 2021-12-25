from geoloc import CurlLocationFetcher

# To fetch using curl location fetcher
location_details = CurlLocationFetcher().fetch()
print(f"Current Location : \n{location_details}")
