class WharfageDueOutports:
    def __init__(self, total_mt: float) -> None:
        self.total_mt = total_mt

    def calculate_wd_outports(self, wd_rate: float) -> float:
        total_wd = round(
            self.total_mt * wd_rate, 2
        )
        return total_wd


class WDOutportsViaShipside(WharfageDueOutports):
    def __init__(self, total_mt: float) -> None:
        super().__init__(total_mt)
        self.wd_rate = 17.00

    def calculate_wd_outport_via_shipside(self) -> float:
        return self.calculate_wd_outports(self.wd_rate)


class WDOutportsViaPierside(WharfageDueOutports):
    def __init__(self, total_mt: float) -> None:
        super().__init__(total_mt)
        self.wd_rate = 34.00

    def calculate_wd_outport_via_pierside(self) -> float:
        return self.calculate_wd_outports(self.wd_rate)
