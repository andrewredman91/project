
from db.run_sql import run_sql
from models.league import League
from models.match import Match
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository


def save(team):
    #print(type(team))
    sql = "INSERT INTO league (team_id,points) VALUES (%s, %s) RETURNING id"
    values = [team.id, 0]
    results = run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM league"
    run_sql(sql)

def select_all():
    leagues = [] 
    sql = "SELECT * FROM league ORDER BY position ASC"
    results = run_sql(sql)
    for result in results:
        team = team_repository.select(result["team_id"])
        league = League(result["position"], team, result["points"])
        leagues.append(league)
    return leagues

#ASSUMES a league exists
def update(home_team, away_team, home_points, away_points):
#    print(league.__dict__)
    sql = "select * from league where team_id = %s"
    values = [home_team]
    existing_results_home_team = run_sql(sql, values)[0]

    values = [away_team]
    existing_results_away_team = run_sql(sql, values)[0]


    if(len(existing_results_home_team)>0):
        points_home_result = existing_results_home_team["points"]
        points_home_result += home_points

    points_away_result = existing_results_away_team["points"]
    points_away_result += away_points

    if(len(existing_results_away_team)>0):
        points_away_result = existing_results_home_team["points"]
        points_away_result += away_points

    sql = "update league set points = %s where team_id = %s"


    values = [points_home_result,home_team]
    #print(sql)
    #print(values)
    results = run_sql(sql, values)

    values = [points_away_result,away_team]
    #print(sql)
    #print(values)
    results = run_sql(sql, values)
        

    #function to sort the positions
    sort_positions()   
    # you decide if you want to be able to add new teams to the league
    # else:
    #     sql = "INSERT INTO league (team, points) VALUES (%s, %s, %s) RETURNING id"
    #     values = [bana1,bana2,teams.name]
    #     results = run_sql(sql, values)
    #if it finds it . ie if len(results )> 0
    # then do an updatre
    # 
    # else
    # do an insert
    
    # print(results)
    # id = results[0]['id']
    # league.id = id

def sort_positions():
    sql = "select * from league order by points desc" 
    existing_results_home_team = run_sql(sql)
    counter = 1
    for result in existing_results_home_team:
        sql = "update league set position = %s where team_id = %s"
        values = [counter,result["team_id"]]
        results = run_sql(sql, values)
        counter +=1