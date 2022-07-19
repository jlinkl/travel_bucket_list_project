from db.run_sql import run_sql
from models.visit import Visit
import repositories.attraction_repository as attraction_repository

def save(visit):
    sql = "INSERT INTO visits (attraction_id, visited, wants_to_visit) VALUES (%s, %s, %s) RETURNING *"
    values = [visit.attraction.id, visit.visited, visit.wants_to_visit]
    results = run_sql(sql, values)
    id = results[0]['id']
    visit.id = id
    return visit

def select_by_attraction_id(id):
    visit = None

    sql = "SELECT * FROM visits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        attraction = attraction_repository.select(row['attraction_id'])
        visit = Visit(attraction, row['visited'], row['wants_to_visit'])
    return visit

def update(visit):
    sql = "UPDATE visits SET (visited, wants_to_visit) = (%s, %s) WHERE attraction_id = %s"
    values = [visit.visited, visit.wants_to_visit, visit.attraction.id]
    run_sql(sql, values)