from db.run_sql import run_sql
from models.match import Match
import repositories.team_repository as team_repository

def save(match):
    print(match.__dict__)
    sql = "INSERT INTO matches (home_team_id, away_team_id, home_score, away_score) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [match.home_team.id, match.away_team.id, match.home_score, match.away_score]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    match.id = id


def select_all():
    matches = []
    sql = "SELECT * FROM matches"
    results = run_sql(sql)
    for result in results:
        home_team = team_repository.select(result["home_team_id"])
        away_team = team_repository.select(result["away_team_id"])
        match = Match(home_team, away_team, result["home_score"], result["away_score"], result["id"])
        matches.append(match)
    return matches


def select(id):
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    home_team = team_repository.select(result["home_team_id"])
    away_team = team_repository.select(result["away_team_id"])
    match = Match(home_team, away_team, result['home_score'],result['away_score'], result["id"])
    return match


def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(match):
    sql = "UPDATE matches SET (home_team_id, away_team_id, home_score, away_score) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team.id, match.away_team.id, match.home_score, match.away_score, match.id]
    run_sql(sql, values)