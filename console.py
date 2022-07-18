import pdb
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()

country1 = Country("Scotland")
country_repository.save(country1)

country2 = Country("England")
country_repository.save(country2)

country3 = Country("Wales")
country_repository.save(country3)

country4 = Country("Ireland")
country_repository.save(country4)

city1 = City("Edinburgh", country1)
city_repository.save(city1)

city2 = City("London", country2)
city_repository.save(city2)

city3 = City("Cardiff", country3)
city_repository.save(city3)

city4 = City("Dublin", country4)
city_repository.save(city4)

pdb.set_trace()