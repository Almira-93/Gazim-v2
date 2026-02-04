from flask import Flask, render, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render("index.html")

@app.route("/register")
def register():
    return render("register.html")

@app.route("/login")
def login():
    return render("login.html")

@app.route("/about")
def about():
    return render("about.html")

@app.route("/story")
def story():
    return render("story.html")

@app.route("/careers")
def careers():
    return render("careers.html")

@app.route("/policy")
def policy():
    return render("policy.html")

@app.route("/terms")
def terms():
    return render("terms.html")

@app.route("/register-user", methods=["POST"])
def register_user():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    print("New Registration ->", username, email)
    
    return "Registration received! (Backend working)"

@app.route("/login-user", methods=["POST"])
def login_user():
    email = request.form.get("email")
    password = request.form.get("password")

    print("Login Attempt ->", email)

    return "Login received! (Backend working)"

if __name__ == "__main__":
    app.run(debug=True)