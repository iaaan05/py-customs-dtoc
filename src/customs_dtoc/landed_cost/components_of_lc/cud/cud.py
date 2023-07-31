class CustomsDuty:
    def __init__(self, dutiable_value: float, rate_of_duty: float) -> None:
        self.dutiable_value = dutiable_value
        self.rate_of_duty = rate_of_duty

    def calculate_cud(self) -> float:
        total_customs_duty = round(
            self.dutiable_value * (self.rate_of_duty / 100), 2
        )
        return total_customs_duty
