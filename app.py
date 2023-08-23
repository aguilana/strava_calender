from flask import Flask, render_template
from strava_api import get_strava_data

app = Flask(__name__)


@app.route("/")
def index():
    runs = get_strava_data()
    return render_template("index.html", runs=runs)


if __name__ == "__main__":
    app.run(debug=True)
