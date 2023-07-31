class ProRataIndividual:
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        self.individual_fob = individual_fob
        self.total_fob = total_fob

    def calculate_pro_rata_individual(self, total_individual_value: float) -> float:
        total_pro_rata_value = round(
            (self.individual_fob / self.total_fob) * total_individual_value, 2
        )
        return total_pro_rata_value


class ProRataIndividualFreight(ProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float, total_frt: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_frt = total_frt

    def calculate_pro_rata_individual_freight(self) -> float:
        return self.calculate_pro_rata_individual(self.total_frt)


class ProRataIndividualInsurance(ProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float, total_ins: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_ins = total_ins

    def calculate_pro_rata_individual_insurance(self) -> float:
        return self.calculate_pro_rata_individual(self.total_ins)


class ProRataIndividualDutiableValue(ProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float, total_dutiable_value: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_dutiable_value = total_dutiable_value

    def calculate_pro_rata_individual_dutiable_value(self) -> float:
        return self.calculate_pro_rata_individual(self.total_dutiable_value)


class ProRataIndividualMiscExpenses(ProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float, total_misc_expenses: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_misc_expenses = total_misc_expenses

    def calculate_pro_rata_individual_misc_expenses(self) -> float:
        return self.calculate_pro_rata_individual(self.total_misc_expenses)
