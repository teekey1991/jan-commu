from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
       return render_template("index.html")

    # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
        message = "講義なう"
        return render_template("index.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
       return render_template("login.html")

    # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
        "ログイン認証"
        return render_template("login.html",)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
       return render_template("register.html")

    # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
        "ログイン認証"
        return render_template("register.html",)



if __name__ == '__main__':
    app.run(port=5000, debug=True)