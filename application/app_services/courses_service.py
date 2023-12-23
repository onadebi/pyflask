import json;
import os;
from application import mongoCon

class CoursesService():
    def __init__(self):
        self.courses: list = [];
        json_file_path = os.path.join(os.getcwd(), 'application','models', 'courses.json');
        print(f'\n***CWD:: {json_file_path} ***\n')
        try:
            with open(json_file_path,'r') as json_file:
                if os.path.exists(json_file_path):                
                    self.courses = json.load(json_file);
        except FileNotFoundError:
            print(f'\n***File not found ERROR:: {json_file_path} ***\n');
        except Exception as error:
            print(f'\n***ERROR:: {error} ***\n');
        
        cursor =mongoCon.db.get_collection('course').find({});
        self.all_courses = [document for document in cursor];

    def get_courses(self) -> list[dict[str,str]]:
        return self.all_courses;

    def get_course_by_CourseId(self, index: int) -> dict[str,str]:
        return next((course for course in self.all_courses if course["courseID"] == str(index)), {});
