class Student:
    def __init__(self, student_id, name, age, gender, branch, year, phone, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.branch = branch
        self.year = year
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "branch": self.branch,
            "year": self.year,
            "phone": self.phone,
            "email": self.email
        }