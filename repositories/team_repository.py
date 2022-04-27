from db.run_sql import run_sql
from models.team import Team

def save(teams):
    sql = "INSERT INTO teams (name) VALUES (%s) RETURNING id"
    values = [teams.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    teams.id = id


def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["name"], result["id"])
        teams.append(team)
    return teams


def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    teams = Team(result["name"], result["id"])
    return teams


def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (name) = (%s) WHERE (id) = (%s)"
    values = [team.name, team.id]
    run_sql(sql, values)