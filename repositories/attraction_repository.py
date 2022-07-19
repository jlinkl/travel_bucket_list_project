from optparse import Values
from models.attraction import Attraction
from db.run_sql import run_sql
import repositories.city_repository as city_repository

def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], city, row['id'])
        attractions.append(attraction)
    return attractions

def delete_all():
    run_sql("DELETE FROM attractions")

def save(attraction):
    sql = "INSERT INTO attractions (name, city_id) VALUES (%s, %s) RETURNING *"
    values = [attraction.name, attraction.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    attraction.id = id
    return attraction

def select_by_city(city):
    attractions = []

    sql = "SELECT * FROM attractions WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    if results is not None:
        for row in results:
            attraction = Attraction(row['name'], city, row['id'])
            attractions.append(attraction)
    return attractions

def select(id):
    city = None

    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], city, row['id'])

    return attraction

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(attraction):
    sql = "UPDATE attractions SET (name, city_id) = (%s, %s) WHERE id = %s"
    values = [attraction.name, attraction.city.id, attraction.id]
    run_sql(sql, values)

def select_visited():
    visited = []

    sql = "SELECT * FROM visits WHERE visited = TRUE"
    results = run_sql(sql)

    for row in results:
        id = row['attraction_id']
        location = select(id)
        visited.append(location)

    return visited
