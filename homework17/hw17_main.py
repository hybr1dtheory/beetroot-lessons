from task1 import Animal, Dog, Cat, speak
from task2 import Author, Library


# Task 1 testing
a = Animal()
d = Dog()
c = Cat()
for animal in (a, d, c):
    speak(animal)

# Task 2 testing
lib = Library("my library")
au = Author("George Orwell", "Great Britain", "25-06-1903")
lib.new_book("1984", 1949, au)
lib.new_book("Animal farm", 1945, au)
lib.new_book("Homage to Catalonia", 1938, au)
au2 = Author("William Faulkner", "USA", "25-09-1897")
lib.new_book("Knight’s Gambit", 1949, au2)
print(lib, end="\n\n")
print(*lib.group_by_author(au), sep='\n', end='\n\n')
print(*lib.group_by_year(1949), sep='\n')
print(lib.get_book_amount())
