class Employee:
    """
    Родительский класс Employee, который содержит общие атрибуты
    и методы для всех сотрудников.
    Методы:
    salary: вычисляет зарплату сотрудника на основе МРОТ, цены за задачу
    и количества выполненных задач.
    info: возвращает строку с информацией о сотруднике,
    включая его имя и зарплату.
    """
    def __init__(self, name, task_price, completed_tasks, min_wage):
        self.name = name
        self.task_price = task_price
        self.completed_tasks = completed_tasks
        self.min_wage = min_wage

    @property
    def salary(self):
        return (self.min_wage +
                int(0.3 * self.task_price * self.completed_tasks))

    def info(self):
        return f'Имя: {self.name}, Зарплата: {self.salary}'


class Manager(Employee):
    """
    Класс Manager, представляющий менеджера, наследуется от Employee.
    Методы:
    salary: вычисляет зарплату менеджера на основе МРОТ, цены за задачу,
    количества выполненных задач, бонуса и количества лет в должности.
    """
    def __init__(self, name, task_price, completed_tasks,
                 min_wage, bonus, years_in_role):
        super().__init__(name, task_price, completed_tasks, min_wage)
        self.bonus = bonus
        self.years_in_role = years_in_role

    @property
    def salary(self):
        return (super().salary + self.bonus * self.years_in_role)


class Developer(Employee):
    """
    Класс Developer, представляющий разработчика, наследуется от Employee.
    Методы:
    salary: вычисляет зарплату разработчика на основе МРОТ, цены за задачу,
    количества выполненных задач,
    бонуса, стейджа и часов сверхурочного времени.
    """
    def __init__(self, name, task_price, completed_tasks,
                 min_wage, bonus, rank, overtime_hours, overtime_rate):
        super().__init__(name, task_price, completed_tasks, min_wage)
        self.bonus = bonus
        self.rank = rank
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    @property
    def salary(self):
        return (super().salary + self.bonus * self.rank +
                self.overtime_hours * self.overtime_rate)
