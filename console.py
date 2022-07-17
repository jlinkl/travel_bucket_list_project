import pdb
from models.country import Country
import repositories.country_repository as country_repository

country_repository.delete_all()

country1 = Country("Scotland")
country_repository.save(country1)

country2 = Country("England")
country_repository.save(country2)

country3 = Country("Wales")
country_repository.save(country3)

country4 = Country("Ireland")
country_repository.save(country4)



pdb.set_trace()