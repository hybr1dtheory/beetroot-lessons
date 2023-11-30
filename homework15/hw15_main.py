from hw15_classes import *

# Task 1
dude = Person("Guido", "Van Rossum", 67)
dude.talk()

# Task 2
my_dog = Dog(12)
print("Age in human equivalent: ", my_dog.human_age())

# Task 3
channels = ["BBC", "Discovery", "TV1000"]
controller = TVController(channels)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))
