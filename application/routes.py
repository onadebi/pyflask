from . import app;
from flask import render_template;
from .app_services.courses_service import CoursesService as courseSvc;

@app.route("/")
@app.route("/index")
@app.route("/home")
def index() -> str:
    return render_template("index.html",title="Home",login_status={'logged_in':False});


@app.route("/login")
def login():
    return render_template("login.html",title="Login");

@app.route("/courses")
def courses():
    courseData: list = courseSvc().get_courses(); 
    print(f'\n*** {courseData[3]["title"]} ***\n')
    return render_template("courses.html",title="Courses",courseData=courseData, courses = True );

@app.route("/register")
def register():
    return render_template("register.html",title="Register");