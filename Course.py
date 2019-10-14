class Course:
    def __init__(self, courseNum, section, courseName, professor):
        self.courseNum = courseNum
        self.section = section
        self.courseName = courseName
        self.professor = professor

    def __str__(self):
        return 'Course: ' + courseNum + section + ' ' + courseName + '; Professor: ' + professor