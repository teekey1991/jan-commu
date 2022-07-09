from flask import Flask, render_template, request
from config import Customer

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

        ID = request.form["Userid"]
        PASS = request.form["Userpassword"]

        for customer in Customer.select():
            if customer.inputEmail == ID and customer.inputPassword == PASS:
                return render_template("index.html", customer=customer)
            else:
                return render_template("register.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        print("Register GET")
        return render_template("register.html")

    # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
        "ログイン認証"
        """新規顧客を追加する関数"""
        # フォーム入力された値に受け取る
        inputEmail = request.form["inputEmail"]
        inputPassword = request.form["inputPassword"]
        lastname = request.form["lastname"]
        farstname = request.form["farstname"]
        lastnamekana = request.form["lastnamekana"]
        farstnamekana = request.form["farstnamekana"]
        inputZip = request.form["inputZip"]
        inputadress = request.form["inputadress"]
        inputage = request.form["inputage"]
        level = request.form["level"]

        # 分割代入でも可
        # [name, age] = request.form

        # 登録処理
        Customer.create(
            inputEmail=inputEmail,
            inputPassword=inputPassword,
            lastname=lastname,
            farstname=farstname,
            lastnamekana=lastnamekana,
            farstnamekana=farstnamekana,
            inputZip=inputZip,
            inputadress=inputadress,
            inputage=inputage,
            level=level,
        )

        print("Register POST")
        return render_template(
            "register.html",
        )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
