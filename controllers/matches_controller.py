from flask import Blueprint, Flask, redirect, render_template, request

from models.match import Match
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

matches_blueprint = Blueprint("matches", __name__)

# INDEX
@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template("matches/index.html", matches=matches)


# NEW
@matches_blueprint.route("/matches/new")
def new_match():
    home_teams = team_repository.select_all()
    teams = team_repository.select_all()
    home_score = match_repository.select_all()
    away_score = match_repository.select_all()
    return render_template("matches/new.html", home_teams=home_teams, teams=teams, home_score=home_score, away_score=away_score)


# CREATE
@matches_blueprint.route("/matches", methods=["POST"])
def create_match():
    home_team_id = request.form["home_team_id"]
    team_id = request.form["team_id"]
    home_team = team_repository.select(home_team_id)
    team = team_repository.select(team_id)
    home_score = request.form["home_score"]
    away_score = request.form["away_score"]
    
    new_match = Match(home_team, team, home_score, away_score)
    match_repository.save(new_match)
    return redirect("/matches")


# EDIT
@matches_blueprint.route("/matches/<id>/edit")
def edit_match(id):
    match = match_repository.select(id)
    teams = team_repository.select_all()
    return render_template('matches/edit.html', match=match, teams=teams)


# UPDATE
@matches_blueprint.route("/matches/<id>", methods=["POST"])
def update_match(id):
    home_team_id = request.form["home_team"]
    away_team_id = request.form["away_team"]
    home_team = team_repository.select(home_team_id)
    away_team = team_repository.select(away_team_id)


    match = Match(home_team, away_team, request.form["home_score"], request.form["away_score"], id)
    match_repository.update(match)
    return redirect("/matches")


# DELETE
@matches_blueprint.route("/matches/<id>/delete", methods=["POST"])
def delete_match(id):
    match_repository.delete(id)
    return redirect("/matches")
