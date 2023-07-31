import math


class DutiableValue:
    def __init__(self, fob_fca_value: float, dutiable_ins: float, dutiable_frt: float,
                 rate_of_exchange: float) -> None:
        self.fob_fca_value = fob_fca_value
        self.dutiable_ins = dutiable_ins
        self.dutiable_frt = dutiable_frt
        self.rate_of_exchange = rate_of_exchange

    def calculate_dutiable_value(self) -> float:
        dutiable_value = (
            self.fob_fca_value, self.dutiable_ins, self.dutiable_frt,
        )
        dutiable_value = round(math.fsum(dutiable_value) * self.rate_of_exchange, 2)
        return dutiable_value


class DutiableValueBySea(DutiableValue):
    def __init__(self, fob_fca_value: float, dutiable_ins: float, dutiable_frt: float,
                 rate_of_exchange: float) -> None:
        super().__init__(fob_fca_value, dutiable_ins, dutiable_frt, rate_of_exchange)

    def calculate_dutiable_value_by_sea(self):
        return self.calculate_dutiable_value()


class DutiableValueByAir(DutiableValue):
    def __init__(self, fob_fca_value: float, dutiable_ins: float, dutiable_frt: float,
                 rate_of_exchange: float) -> None:
        super().__init__(fob_fca_value, dutiable_ins, dutiable_frt, rate_of_exchange)

    def calculate_dutiable_value_by_air(self):
        return self.calculate_dutiable_value()
