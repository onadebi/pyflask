import json;
import os;

class CoursesService():
    def __init__(self):
        self.courses: list = [];
        json_file_path = os.path.join(os.getcwd(), 'application','models', 'courses.json');
        print(f'\n***CWD:: {json_file_path} ***\n')
        try:
            with open(json_file_path,'r') as json_file:
                self.courses = json.load(json_file);
        except FileNotFoundError:
            print(f'\n***File not found ERROR:: {json_file_path} ***\n');
        except Exception as error:
            print(f'\n***ERROR:: {error} ***\n');

    def get_courses(self) -> list[dict[str,str]]:
        return self.courses;

    def get_course_by_CourseId(self, index: int) -> dict[str,str]:
        return next((course for course in self.courses if course["courseID"] == str(index)), {});