from . import app;
from flask import render_template, request, Response;
import json;
from application.app_services.courses_service import CoursesService as courseSvc;
from application.models import User;
from .app_services.user_service import UserService as userSvc;

@app.route("/")
@app.route("/index")
@app.route("/home")
def index() -> str:
    return render_template("index.html",title="Home Page",login_status={'logged_in':False}, index= True);


@app.route("/login")
def login():
    return render_template("login.html",title="Login", login=True);

@app.route("/courses")
@app.route("/courses/<term>")
def courses(term: str = "Spring 2019"):
    courseData: list = courseSvc().get_courses(); 
    print(courseData)
    print(f'\n*** {courseData[0]["title"]} ***\n')
    return render_template("courses.html",title="Courses",courseData=courseData, courses = True, term = term );

@app.route("/enrollment", methods=["GET","POST"])
def enrollment():
    data : dict = {};    # empty dictionary
    if request.method == "GET":
        courseID: str = request.args.get("courseID");
        courseTitle: str = request.args.get("title");
        courseTerm: str = request.args.get("term");
    else:
        courseID: str = request.form.get("courseID");
        courseTitle: str = request.form.get("title");
        courseTerm: str = request.form.get("term");
    data= {"courseID":courseID,"title":courseTitle, "term":courseTerm};    
    return render_template("enrollment.html",title="Enrollment",data=data, enrollment=True);

@app.route("/register")
def register():
    # userSvc().create_user({'first_name': 'Onadebi', 'last_name': 'Onax'})
    return render_template("register.html",title="Register", register=True);


#region API Routes
@app.route("/api/")
@app.route("/api/<idx>")
def api(idx: int =None):
    if(idx==None):
        jData = courseSvc().get_courses();
    else:
        jData = courseSvc().get_course_by_CourseId(int(idx));
    return Response(json.dumps(jData), mimetype="application/json");



#endregion

@app.route("/user")
def user():
    user_profile: User = {
        'user_id' : 2,
        'first_name':"Christian",
        'last_name':"Hur",
        'email':"christian_hur@onaxsys.com",
        'password':"123abcd"
    }
    # objRes = userSvc().add(user_profile);

    return render_template('user.html', users = userSvc().get_all_users(), title=' All Users.', user=True)