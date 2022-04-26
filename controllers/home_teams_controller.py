from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository

home_teams_blueprint = Blueprint("home_teams", __name__)

# INDEX
@home_teams_blueprint.route("/home_teams")
def home_teams():
    home_teams = team_repository.select_all()
    return render_template("home_teams/index.html", home_teams=home_teams)


# NEW
@home_teams_blueprint.route("/home_teams/new")
def new_home_team():
    return render_template("home_teams/new.html")


# CREATE
@home_teams_blueprint.route("/home_teams", methods=["POST"])
def create_home_team():
    name = request.form["name"]
    new_home_team = Team(name)
    team_repository.save(new_home_team)
    return redirect("/home_teams")


# EDIT
@home_teams_blueprint.route("/home_teams/<id>/edit")
def edit_home_team(id):
    home_team = team_repository.select(id)
    return render_template('home_teams/edit.html', home_team=home_team)


# UPDATE
@home_teams_blueprint.route("/home_teams/<id>", methods=["POST"])
def update_home_team(id):
    name = request.form["name"]
    home_team = Team(name, id)
    team_repository.update(home_team)
    return redirect("/home_teams")


# DELETE
@home_teams_blueprint.route("/home_teams/<id>/delete", methods=["POST"])
def delete_home_team(id):
    team_repository.delete(id)
    return redirect("/home_teams")
