from task1 import Teacher, Student
from task2 import Mathematician
from task3 import ProductStore, Product
from task4 import NotInRangeError, test_except


# Task 1 testing
stud = Student("Alex", "Petrenko", 2002, 1, "CS-23", 1500)
print(stud.get_person_info())
print(stud.get_student_info())
print(stud.calculate_scholarship(4.2))

teacher = Teacher("Oleh", "Sachko", 1987, 22, "Math teacher", 1100)
print(teacher.get_person_info())
print(teacher.get_employee_info())
print(teacher.calculate_salary(21))

# Task 2 testing
print("\n\nTask 2\n")
m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020, 2100]))

# Task 3 testing
print("\n\nTask 3\n")
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
print(*s.get_all_products(), sep='')
print(s.get_income())
s.sell_product('Ramen', 10)
print(s.get_product_info('Ramen'))
s.set_discount("Football T-Shirt", 50)
print(*s.get_all_products(), sep='')

# Task 4 testing
try:
    print(test_except(1, 10, 100))
except NotInRangeError as e:
    print(e)
