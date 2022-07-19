import pdb
from models.country import Country
from models.city import City
from models.attraction import Attraction
from models.visit import Visit
from models.user import User
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository
import repositories.visit_repository as visit_repository
import repositories.user_repository as user_repository

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

attraction1 = Attraction("Scott Monument", city1)
attraction_repository.save(attraction1)

attraction2 = Attraction("Big Ben", city2)
attraction_repository.save(attraction2)

attraction3 = Attraction("Cardiff Castle", city3)
attraction_repository.save(attraction3)

attraction4 = Attraction("Irish Whiskey Museum", city4)
attraction_repository.save(attraction4)

visit1 = Visit(attraction1, True, False)
visit_repository.save(visit1)

visit2 = Visit(attraction2, True, False)
visit_repository.save(visit2)

visit3 = Visit(attraction3, False, True)
visit_repository.save(visit3)

visit4 = Visit(attraction4, False, True)
visit_repository.save(visit4)

# user1 = User("James")
# user_repository.save(user1)

# user2 = User("Tom")
# user_repository.save(user2)

pdb.set_trace()