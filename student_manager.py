from student import Student
from file_handler import load_students, save_students
from tabulate import tabulate
import re
from logger_config import log_info, log_error

class StudentManager:

    def __init__(self):
        self.students = load_students()


    # ---------------- VALIDATIONS ----------------

    def validate_student_id(self, student_id):
        return student_id.isdigit()


    def validate_age(self, age):
        return 15 <= age <= 60


    def validate_gender(self, gender):
        return gender.lower() in ["male", "female", "other"]


    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10


    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)



    # ---------------- ADD STUDENT ----------------

    def add_student(self):

        student_id = input("Enter Student ID: ")

        if not self.validate_student_id(student_id):
            print("❌ Student ID must contain only numbers")
            return


        for student in self.students:
            if student["student_id"] == student_id:
                print("❌ Student ID already exists!")
                return


        name = input("Enter Name: ")

        if not name.strip():
            print("❌ Name cannot be empty")
            return



        try:
            age = int(input("Enter Age: "))

            if not self.validate_age(age):
                print("❌ Age should be between 15 and 60")
                return

        except ValueError:
            print("❌ Age must be a number")
            return



        gender = input("Enter Gender: ")

        if not self.validate_gender(gender):
            print("❌ Gender should be Male/Female/Other")
            return



        branch = input("Enter Branch: ")
        year = input("Enter Year: ")



        phone = input("Enter Phone Number: ")

        if not self.validate_phone(phone):
            print("❌ Phone number must contain exactly 10 digits")
            return



        email = input("Enter Email: ")

        if not self.validate_email(email):
            print("❌ Invalid email format")
            return



        student = Student(
            student_id,
            name,
            age,
            gender,
            branch,
            year,
            phone,
            email
        )


        self.students.append(student.to_dict())

        save_students(self.students)

        print("✅ Student Added Successfully!")

        log_info(f"Student Added: {student_id}")



    # ---------------- VIEW STUDENTS ----------------

    def view_students(self):

        if not self.students:
            print("No student records found.")
            return


        table = []

        for student in self.students:
            table.append([
                student["student_id"],
                student["name"],
                student["age"],
                student["gender"],
                student["branch"],
                student["year"],
                student["phone"],
                student["email"]
            ])


        headers = [
            "ID",
            "Name",
            "Age",
            "Gender",
            "Branch",
            "Year",
            "Phone",
            "Email"
        ]


        print("\n===== Student Records =====")

        print(
            tabulate(
                table,
                headers=headers,
                tablefmt="grid"
            )
        )



    # ---------------- SEARCH STUDENT ----------------

    def search_student(self):

        keyword = input("Enter Student ID or Name: ").lower()

        found = False


        for student in self.students:

            if (
                student["student_id"].lower() == keyword
                or student["name"].lower() == keyword
            ):

                print("\nStudent Found:")

                print(
                    tabulate(
                        [student.values()],
                        headers=student.keys(),
                        tablefmt="grid"
                    )
                )

                found = True



        if not found:
            print("❌ Student not found")



    # ---------------- UPDATE STUDENT ----------------

    def update_student(self):

        student_id = input("Enter Student ID to Update: ")


        for student in self.students:

            if student["student_id"] == student_id:

                print("Leave blank to keep old value")


                name = input(
                    f"Name ({student['name']}): "
                )

                if name:
                    student["name"] = name



                age = input(
                    f"Age ({student['age']}): "
                )

                if age:

                    try:
                        age = int(age)

                        if self.validate_age(age):
                            student["age"] = age
                        else:
                            print("❌ Invalid age")
                            return

                    except ValueError:
                        print("❌ Age must be number")
                        return




                phone = input(
                    f"Phone ({student['phone']}): "
                )

                if phone:

                    if self.validate_phone(phone):
                        student["phone"] = phone
                    else:
                        print("❌ Invalid phone number")
                        return



                email = input(
                    f"Email ({student['email']}): "
                )

                if email:

                    if self.validate_email(email):
                        student["email"] = email
                    else:
                        print("❌ Invalid email")
                        return



                save_students(self.students)

                print("✅ Student Updated Successfully!")

                return
            
            log_info(f"Student Updated: {student_id}")



        print("❌ Student ID not found")



    # ---------------- DELETE STUDENT ----------------

    def delete_student(self):

        student_id = input(
            "Enter Student ID to Delete: "
        )


        for student in self.students:

            if student["student_id"] == student_id:

                self.students.remove(student)

                save_students(self.students)

                print("✅ Student Deleted Successfully!")

                return
            
        log_info(f"Student Deleted: {student_id}")


        print("❌ Student ID not found")