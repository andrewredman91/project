from flask import Flask, render_template

from controllers.matches_controller import matches_blueprint
from controllers.home_teams_controller import home_teams_blueprint
from controllers.away_teams_controller import teams_blueprint

app = Flask(__name__)

app.register_blueprint(matches_blueprint)
app.register_blueprint(home_teams_blueprint)
app.register_blueprint(teams_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
