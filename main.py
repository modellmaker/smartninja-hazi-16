from flask import Flask, render_template, request, make_response

app = Flask(__name__)


class Movies:
    def __init__(self, title, summary, imdb):
        self.title = title
        self.summary = summary
        self.imdb = imdb


egy = Movies("cim", "leiras", "IMDB")
ketto = Movies("cim2", "leiras2", "IMDB2")
harom = Movies("cim3", "leiras3", "IMDB3")
movies = [egy, ketto, harom]
my_dict = {}


@app.route("/")
def index():
    return render_template("index.html")


def openfile():
    with open("users.csv", 'r') as user_file:
        content = user_file.read().splitlines()
        for row in content:
            (username, pwd) = row.split(",")
            my_dict[username] = pwd
        return my_dict


def writefile(username, password):
    with open("users.csv", 'a+') as user_file:
        content = user_file.read().splitlines()
        for row in content:
            (name, pwd) = row.split(",")
            my_dict[name] = pwd
        if username is None:
            pass
        else:
            my_dict.update({username: password})
        user_file.write(str("\n" + username + "," + password))
# my_dict = {"asd@asd.asd": "asd", "joe@joe.joe": "joe", "email@address.com": "pwd1234"}


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    openfile()
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


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    writefile(username, password)
    # print(my_dict)
    message = "You have successfully registered on our page. You can now login."

    response = make_response(render_template("index.html", message=message))

    return response


@app.route("/signup-main", methods=["GET"])
def signup_main():
    response = make_response(render_template("signup.html"))

    return response


if __name__ == "__main__":
    app.run()
