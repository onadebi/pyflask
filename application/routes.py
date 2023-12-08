from . import app;
from flask import render_template;

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html",title="Home",login_status={'logged_in':False});


@app.route("/login")
def login():
    return render_template("login.html",title="Home",login_status={'logged_in':False});

@app.route("/courses")
def courses():
    return render_template("courses.html",title="Home",login_status={'logged_in':False});

@app.route("/register")
def register():
    return render_template("register.html",title="Home",login_status={'logged_in':False});