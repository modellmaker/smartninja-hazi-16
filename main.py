from flask import Flask, render_template, request, make_response

app = Flask(__name__)


class Movies():
    def __init__(self, title, summary, imdb):
        self.title = title
        self.summary = summary
        self.imdb = imdb


egy = Movies("cim", "leiras", "IMDB")
ketto = Movies("cim2", "leiras2", "IMDB2")
harom = Movies("cim3", "leiras3", "IMDB3")
movies = [egy, ketto, harom]


@app.route("/")
def index():
    return render_template("index.html")


my_dict = {"asd@asd.asd": "asd", "joe@joe.joe": "joe", "email@address.com": "pwd1234"}


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in my_dict:
        if my_dict[username] == password:
            response = make_response(render_template("index.html", movies=movies, name=username))
            response.set_cookie("c_username", username)
    else:
        response = render_template("index.html")

    return response


@app.route("/logout", methods=["POST"])
def logout():
    response = make_response(render_template("index.html"))
    response.set_cookie("c_username", expires=0)
    return response


if __name__ == "__main__":
    app.run()
