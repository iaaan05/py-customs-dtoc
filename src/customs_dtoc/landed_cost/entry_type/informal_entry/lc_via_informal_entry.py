import math


class LandedCostViaInformalEntry:
    def __init__(self, dutiable_value: float, customs_duty: float, brokerage_fee: float,
                 customs_documentary_stamps: float) -> None:
        self.dutiable_value = dutiable_value
        self.customs_duty = customs_duty
        self.brokerage_fee = brokerage_fee
        self.customs_documentary_stamps = customs_documentary_stamps
    
    def calculate_landed_cost_via_informal_entry(self) -> float:
        components = (
            self.dutiable_value, self.customs_duty, self.brokerage_fee, self.customs_documentary_stamps
        )
        return round(math.fsum(components), 2)
