import numpy as np

from city import City
from movie import Movie


cities = ['Bordeaux', 'Toulouse', 'Narbonne', 'Pau']
city = City('Toulouse', 500_000)
movie = Movie('The Revenant', 2015)
data = np.random.normal(10.0, 2.5, 1_000_000)

# builtin functions
print("*********** builtin str **************") # public = end user
print('cities [', len(cities), '] :', cities) # call str() for each objects
print(str(cities)) # calls method list.__str__
print(cities.__str__())

print(city) # City.__str__ by default (@dataclass) : City(name='Toulouse', population=500000) 
print(movie) # Movie.__str__ by default (python) : <movie.Movie object at 0x000001B5E34738C0>
print(data) # ndarray.__str__ : [ 9.37019485  8.44084408  9.4516031  ...  6.32187911  7.96062213 14.47753298]

print()
print("*********** builtin repr **************") # public = developer
print(repr(city)) # calls City.__repr__
print(repr(movie))
print(repr(city.name))
print(repr(data))
# operators