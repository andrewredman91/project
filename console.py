from models.match import Match
import repositories.match_repository as match_repository

from models.team import Team
import repositories.team_repository as team_repository

from models.league import League
import repositories.league_repository as league_repository


match_repository.delete_all()
league_repository.delete_all()
team_repository.delete_all()

team_1 = Team("Sweden 🇸🇪")
team_repository.save(team_1)

team_2 = Team("Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿")
team_repository.save(team_2)

team_3 = Team("South Africa 🇿🇦")
team_repository.save(team_3)

team_4 = Team("England 🏴󠁧󠁢󠁥󠁮󠁧󠁿")
team_repository.save(team_4)

team_5 = Team("Columbia 🇨🇴")
team_repository.save(team_5)

team_6 = Team("United States 🇺🇸")
team_repository.save(team_6)

team_7 = Team("Canada 🇨🇦")
team_repository.save(team_7)

team_8 = Team("France 🇫🇷")
team_repository.save(team_8)

team_9 = Team("Spain 🇪🇸")
team_repository.save(team_9)

team_10 = Team("South Korea 🇰🇷")
team_repository.save(team_10)

team_11 = Team("Wales 🏴󠁧󠁢󠁷󠁬󠁳󠁿")
team_repository.save(team_11)


league_repository.save(team_1)
league_repository.save(team_2)
league_repository.save(team_3)
league_repository.save(team_4)
league_repository.save(team_5)
league_repository.save(team_6)
league_repository.save(team_7)
league_repository.save(team_8)
league_repository.save(team_9)
league_repository.save(team_10)
league_repository.save(team_11)

match_1 = Match(team_1, team_10, 1, 1)
match_repository.save(match_1)

match_2 = Match(team_2, team_8, 3, 2)
match_repository.save(match_2)

match_3 = Match(team_3, team_7, 0, 2)
match_repository.save(match_3)

match_4 = Match(team_4, team_9, 0, 1)
match_repository.save(match_4)

match_5 = Match(team_5, team_6, 5, 1)
match_repository.save(match_5)

match_6 = Match(team_6, team_10, 2, 1)
match_repository.save(match_6)

match_7 = Match(team_7, team_1, 0, 3)
match_repository.save(match_7)

match_8 = Match(team_8, team_3, 2, 2)
match_repository.save(match_8)

match_9 = Match(team_9, team_2, 0, 0)
match_repository.save(match_9)

match_10 = Match(team_4, team_5, 0, 7)
match_repository.save(match_10)

match_11 = Match(team_11, team_1, 3, 0)
match_repository.save(match_11)

match_12 = Match(team_11, team_4, 0, 1)
match_repository.save(match_12)

