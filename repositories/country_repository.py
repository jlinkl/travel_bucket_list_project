from db.run_sql import run_sql
from models.country import Country

# SET countries = []
# SET sql = "SELECT ALL FROM countries"
# SET result = run_sql(sql)
# FOR each row IN results
#    SET country = Country(row['name'], row['id'])
#    countries.append(country)
# RETURN countries

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
        country = Country(row['name'], row['id'])

    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def update(country):
    sql = "UPDATE countries SET name = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)

def find_by_name(name):
    country = None

    sql = "SELECT * FROM countries WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        country = Country(row['name'], row['id'])

    return country