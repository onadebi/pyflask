from . import app;
from flask import render_template, request;
from .app_services.courses_service import CoursesService as courseSvc;

@app.route("/")
@app.route("/index")
@app.route("/home")
def index() -> str:
    return render_template("index.html",title="Home",login_status={'logged_in':False}, index= True);


@app.route("/login")
def login():
    return render_template("login.html",title="Login", login=True);

@app.route("/courses")
@app.route("/courses/<term>")
def courses(term: str = "Spring 2019"):
    courseData: list = courseSvc().get_courses(); 
    print(f'\n*** {courseData[3]["title"]} ***\n')
    return render_template("courses.html",title="Courses",courseData=courseData, courses = True, term = term );

@app.route("/enrollment", methods=["GET","POST"])
def enrollment():
    data : dict = {};    # empty dictionary
    if request.method == "GET":
        courseID: str = request.args.get("courseID");
        courseTitle: str = request.args.get("title");
        courseTerm: str = request.args.get("term");
        data= {"courseID":courseID,"title":courseTitle, "term":courseTerm};    
    return render_template("enrollment.html",title="Enrollment",data=data, enrollment=True);

@app.route("/register")
def register():
    return render_template("register.html",title="Register", register=True);