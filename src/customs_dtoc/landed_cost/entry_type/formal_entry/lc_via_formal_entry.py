import math


class LandedCostBySeaViaFormalEntry:
    def __init__(self, dutiable_value: float, customs_duty: float, bank_charge: float, brokerage_fee: float,
                 arrastre_charge: float, wharfage_due: float, import_processing_fee: float,
                 customs_documentary_stamps: float) -> None:
        self.dutiable_value = dutiable_value
        self.customs_duty = customs_duty
        self.bank_charge = bank_charge
        self.brokerage_fee = brokerage_fee
        self.arrastre_charge = arrastre_charge
        self.wharfage_due = wharfage_due
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps

    def calculate_landed_cost_by_sea(self) -> float:
        components = (
            self.dutiable_value, self.customs_duty, self.bank_charge, self.brokerage_fee, self.arrastre_charge,
            self.wharfage_due, self.import_processing_fee, self.customs_documentary_stamps
        )
        return round(math.fsum(components), 2)


class LandedCostByAirViaFormalEntry:
    def __init__(self, dutiable_value: float, customs_duty: float, bank_charge: float, brokerage_fee: float,
                 import_processing_fee: float, customs_documentary_stamps: float) -> None:
        self.dutiable_value = dutiable_value
        self.customs_duty = customs_duty
        self.bank_charge = bank_charge
        self.brokerage_fee = brokerage_fee
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps

    def calculate_landed_cost_by_air(self) -> float:
        components = (
            self.dutiable_value, self.customs_duty, self.bank_charge, self.brokerage_fee,
            self.import_processing_fee, self.customs_documentary_stamps
        )
        return round(math.fsum(components), 2)
