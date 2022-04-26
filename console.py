from models.match import Match
import repositories.match_repository as match_repository

from models.team import Team

from models.team import Team
import repositories.team_repository as team_repository

match_repository.delete_all()
team_repository.delete_all()
team_repository.delete_all()


team_1 = Team("Edinburgh Green")
team_repository.save(team_1)

team_2 = Team("Edinburgh Brown")
team_repository.save(team_2)

team_3 = Team("Glasgow Irish")
team_repository.save(team_3)

team_4 = Team("Glasgow Zombie")
team_repository.save(team_4)

match_1 = Match(team_2, team_3, 1, 0)
match_repository.save(match_1)

match_2 = Match(home_team_3, team_1, 3, 2)
match_repository.save(match_2)

match_3 = Match(home_team_3, team_2, 0, 2)
match_repository.save(match_3)

match_4 = Match(home_team_4, team_2, 0, 1)
match_repository.save(match_4)


