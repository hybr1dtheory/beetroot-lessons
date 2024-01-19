"""This task was initially performed without Lock to understand the problems
that can arise with multithreading. To be honest, in my case (Windows 11 (x64),
Python 3.12 (CPython)) I never got an incorrect result during 30 runs)
But, realising that the counter += 1 operation is not atomic in python
and problems can arise here, I used Lock. """
from threading import Thread, Lock


class Counter(Thread):
    counter = 0
    rounds = 100000
    lock = Lock()

    @classmethod
    def increment(cls):
        with cls.lock:
            cls.counter += 1

    def run(self):
        print(f"{self.name} starts its work")
        for _ in range(self.rounds):
            self.increment()
        print(f"{self.name} finish its work")


num_trd = 3  # number of threads
threads = [Counter(name=f"tread-{i + 1}") for i in range(num_trd)]
for trd in threads:
    trd.start()
for trd in threads:
    trd.join()

print(f"Final counter value = {Counter.counter}")
