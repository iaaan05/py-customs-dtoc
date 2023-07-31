class VatExciseTax:
    def __init__(self, landed_cost: float, excise_tax: float) -> None:
        self.landed_cost = landed_cost
        self.excise_tax = excise_tax
        self.vat_rate = 0.12

    def calculate_vat_with_et(self) -> float:
        total_value_added_tax = round(
            (self.landed_cost + self.excise_tax) * self.vat_rate, 2
        )
        return total_value_added_tax


class VatNonExciseTax:
    def __init__(self, landed_cost: float) -> None:
        self.landed_cost = landed_cost
        self.vat_rate = 0.12

    def calculate_vat_non_excise_tax(self) -> float:
        total_value_added_tax = round(
            self.landed_cost * self.vat_rate, 2
        )
        return total_value_added_tax
