import unittest
from customs_dtoc import LandedCostBySeaViaFormalEntry, LandedCostByAirViaFormalEntry, LandedCostViaInformalEntry


class TestLandedCost(unittest.TestCase):
    def test_lc_formal_entry_sea(self):
        lc_formal_entry_sea = LandedCostBySeaViaFormalEntry(
            dutiable_value=2145621.31, customs_duty=321843.20, bank_charge=2682.03, brokerage_fee=7732.03,
            arrastre_charge=800, wharfage_due=1700, import_processing_fee=1000, customs_documentary_stamps=280
        )
        self.assertEqual(lc_formal_entry_sea.calculate_landed_cost_by_sea(), 2481658.57)

    def test_lc_formal_entry_air(self):
        lc_formal_entry_air = LandedCostByAirViaFormalEntry(
            dutiable_value=2145621.31, customs_duty=321843.20, bank_charge=2682.03, brokerage_fee=7732.03,
            import_processing_fee=1000, customs_documentary_stamps=280
        )
        self.assertEqual(lc_formal_entry_air.calculate_landed_cost_by_air(), 2479158.57)

    def test_lc_informal_entry(self):
        lc_informal_entry = LandedCostViaInformalEntry(
            dutiable_value=2145621.31, customs_duty=321843.20, brokerage_fee=700, customs_documentary_stamps=280
        )
        self.assertEqual(lc_informal_entry.calculate_landed_cost_via_informal_entry(), 2468444.51)


if __name__ == '__main__':
    unittest.main()
