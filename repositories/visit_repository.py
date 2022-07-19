from db.run_sql import run_sql
from models.visit import Visit

def save(visit):
    sql = "INSERT INTO visits (attraction_id, visited, wants_to_visit) VALUES (%s, %s, %s) RETURNING *"
    values = [visit.attraction.id, visit.visited, visit.wants_to_visit]
    results = run_sql(sql, values)
    id = results[0]['id']
    visit.id = id
    return visit
