from flask import Flask, render_template, request
from config import Customer, Post

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        posts = Post.select()
        return render_template("index.html", posts=posts)

    # # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
        #     "検索"
        Customer_email = request.form["Customer_email"]
        Area = request.form["Area"]
        When = request.form["When"]
        Level = request.form["Level"]
        Class = request.form["Class"]
        text = request.form["text"]
        
                # 分割代入でも可
        # [name, age] = request.form

        # 登録処理
        Post.create(
            Customer_email=Customer_email,
            Area=Area,
            When=When,
            Level=Level,
            Class=Class,
            text=text,
        )

        print("index POST")
        return render_template("index.html")


@app.route("/post", methods=["GET", "POST"])
def post():
    email = request.args.get("email")

    if request.method == "GET":
        for customer in Customer.select():
            if email == customer.inputEmail:
                return render_template("post.html", customer=customer, email=email)

    # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
        email = request.form["email"]
        #     for customer in Customer.select():
        #         if customer == customer.inputEmail:
        #             email = customer.inputEmail
        #     "検索"
        Area = request.form["Area"]
        When = request.form["When"]
        Level = request.form["Level"]
        Class = request.form["Class"]
        text = request.form["text"]

        Post.create(
            Customer_email=email,
            Area=Area,
            When=When,
            Level=Level,
            Class=Class,
            text=text,
        )

        print("index POST")
        return render_template("index.html")


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
                return render_template("login.html")


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
        firstname = request.form["firstname"]
        lastnamekana = request.form["lastnamekana"]
        firstnamekana = request.form["firstnamekana"]
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
            firstname=firstname,
            lastnamekana=lastnamekana,
            firstnamekana=firstnamekana,
            inputZip=inputZip,
            inputadress=inputadress,
            inputage=inputage,
            level=level,
        )

        print("Register POST")
        return render_template(
            "register.html",
        )


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        print("home GET")
        return render_template("home.html")

    # もしPOSTリクエストだった場合はindex.htmlでmessage変数を使う
    if request.method == "POST":
       
        print("home POST")
        return render_template(
            "home.html",
        )


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
