from flask import Blueprint, Flask, redirect, render_template, request

from models.league import League
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

leagues_blueprint = Blueprint("leagues", __name__)

# INDEX
@leagues_blueprint.route("/leagues")
def leagues():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)