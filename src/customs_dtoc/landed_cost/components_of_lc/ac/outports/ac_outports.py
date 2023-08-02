class ArrastreChargeOutports:
    def __init__(self, total_metric_ton: float) -> None:
        self.total_metric_ton = total_metric_ton

    def calculate_ac_outports(self, ac_rate: float) -> float:
        total_ac = round(
            self.total_metric_ton * ac_rate, 2
        )
        return total_ac


class ACOutportsViaShipside(ArrastreChargeOutports):
    def __init__(self, total_metric_ton: float) -> None:
        super().__init__(total_metric_ton)
        self.ac_rate = 8.00

    def calculate_ac_outport_via_shipside(self) -> float:
        return self.calculate_ac_outports(self.ac_rate)


class ACOutportsViaPierside(ArrastreChargeOutports):
    def __init__(self, total_metric_ton: float) -> None:
        super().__init__(total_metric_ton)
        self.ac_rate = 110.00

    def calculate_ac_outport_via_pierside(self) -> float:
        return self.calculate_ac_outports(self.ac_rate)
