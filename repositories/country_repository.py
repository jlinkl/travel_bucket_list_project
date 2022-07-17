from db.run_sql import run_sql
from models.country import Country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None

    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        country = Country[row['name'], row['id']]

    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country