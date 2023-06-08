class Counter:
    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start: int) -> None:
        self.current = start

    def set_max(self, max_value: int) -> None:
        self.max_value = max_value

    def set_min(self, min_value: int) -> None:
        self.min_value = min_value

    def step_up(self) -> None:
        if self.current < self.max_value:
            self.current += 1
        else:
            print("Досягнутий максимум")

    def step_down(self) -> None:
        if self.current > self.min_value:
            self.current -= 1
        else:
            print("Досягнутий мінімум")

    def get_current(self) -> int:
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7
