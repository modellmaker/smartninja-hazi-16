from flask import Flask, render_template

app = Flask(__name__)


class Movies():
    def __init__(self, title, summary, imdb):
        self.title = title
        self.summary = summary
        self.imdb = imdb


egy = Movies("cim", "leiras", "IMDB")
ketto = Movies("cim2", "leiras2", "IMDB2")
harom = Movies("cim3", "leiras3", "IMDB3")


@app.route("/")
def index():
    movies = [egy, ketto, harom]
    return render_template("index.html", movies=movies)


if __name__ == "__main__":
    app.run()
