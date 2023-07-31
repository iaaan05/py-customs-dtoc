class BankCharge:
    def __init__(self, dutiable_value: float) -> None:
        self.dutiable_value = dutiable_value
        self.bc_rate = 0.00125

    def calculate_bc(self) -> float:
        bc = round(
            self.dutiable_value * self.bc_rate, 2
        )
        return bc
