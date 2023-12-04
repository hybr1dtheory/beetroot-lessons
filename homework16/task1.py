class Person:
    """Base class for students and teachers"""
    def __init__(self, name: str, surname: str, year_of_birth: int):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth

    def get_person_info(self):
        return f"Name: {self.name} {self.surname} \nYear of birth: {self.year_of_birth}"


class Teacher(Person):
    def __init__(self, name: str, surname: str, year_of_birth: int, employee_id: int,
                 position: str, day_salary: float):
        super().__init__(name, surname, year_of_birth)
        self.employee_id = employee_id
        self.position = position
        self.salary = day_salary

    def calculate_salary(self, workdays: int):
        return self.salary * workdays

    def get_employee_info(self):
        p_info = self.get_person_info()
        return f"ID: {self.employee_id} \n{p_info} \nPosition: {self.position} \nSalary per day: {self.salary}\n"


class Student(Person):
    def __init__(self, name: str, surname: str, year_of_birth: int, student_id: int,
                 group: str, scholarship: float):
        super().__init__(name, surname, year_of_birth)
        self.student_id = student_id
        self.group = group
        self.scholarship = scholarship

    def calculate_scholarship(self, avg_grade: float):
        if avg_grade >= 4.5:
            return self.scholarship * 1.2
        elif avg_grade >= 4:
            return self.scholarship
        else:
            return 0

    def get_student_info(self):
        p_info = self.get_person_info()
        return f"Student ID: {self.student_id} \n{p_info} \nGroup: {self.group} \nScholarship: {self.scholarship}\n"
