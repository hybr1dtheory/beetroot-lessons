class Boss:
    """Represents a manager who has a certain number of subordinate workers"""
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def get_workers(self):
        return self.__workers.copy()

    def add_worker(self, *workers):
        for worker in workers:
            if isinstance(worker, Worker):
                self.__workers.append(worker)
            else:
                raise ValueError("Only instance of the class Worker can be added to workers list")


class Worker:
    """Represents an employee who is subordinated to a line manager"""
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Company: {self.company}, Boss: {self.boss.name}"

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self.__boss = boss
        else:
            raise ValueError('Attribute boss must be an instance of the class Boss')
