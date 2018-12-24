class Student:
    def __init__(self, email, s_name, s_password):
        self._email=email
        self._s_name=s_name
        self._s_password=s_password

    def get_email(self):
        return self._email
    
    def set_email(self,new_email):
#         print("The email changed from {}, to {}".format(self._email,new_email))
        self._email=new_email
        
    def get_password(self):
        return self._s_password
    
    def set_password(self,new_pass):
        self._s_password=new_pass
        

class Course:
    def __init__(self,c_id,c_name,instructor):
        self._c_id=c_id
        self._c_name=c_name
        self._instructor=instructor
        
    def get_id(self):
        return self._c_id
    
    def set_id(self,new_id):
        self._c_id=new_id
    
    def get_name(self):
        return self._c_name
    
    def set_name(self, new_name):
        self._c_name=new_name
        
    def get_instructor(self):
        return self._instructor
    
    def set_instructor(self,new_instructor):
        self._instructor=new_instructor
    
class Attending:
    def __init__(self, course_id, student_email):
        self._course_id=course_id
        self._student_email=student_email
    
    def get_course_id(self):
        return self._course_id
    
    def set_course_id(self,new_c_id):
        self._course_id=new_c_id
    
    def get_student_email(self):
        return self._student_email
    
    def set_student_email(self,new_s_email):
        self._student_email=new_s_email
