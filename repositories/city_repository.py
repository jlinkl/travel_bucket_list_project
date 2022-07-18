from optparse import Values
from models.city import City
from db.run_sql import run_sql
import repositories.country_repository as country_repository

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['id'])
        cities.append(city)
    return cities

def delete_all():
    run_sql("DELETE FROM cities")

def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (%s, %s) RETURNING *"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_by_country(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    if results is not None:
        for row in results:
            city = City(row['name'], country, row['id'])
            cities.append(city)
    return cities

def select(id):
    city = None

    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['id'])

    return city
