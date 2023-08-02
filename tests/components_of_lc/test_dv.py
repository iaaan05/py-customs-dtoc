import unittest
from customs_dtoc import DutiableValueBySea, DutiableValueByAir


class TestDutiableValue(unittest.TestCase):
    def test_dv_sea(self):
        dv_sea = DutiableValueBySea(
            fob_fca_value=20000, dutiable_ins=700, dutiable_frt=2500, rate_of_exchange=55.45
        )
        self.assertEqual(dv_sea.calculate_dutiable_value_by_sea(), 1286440.0)

    def test_dv_air(self):
        dv_air = DutiableValueByAir(
            fob_fca_value=20000, dutiable_ins=700, dutiable_frt=2500, rate_of_exchange=55.45
        )
        self.assertEqual(dv_air.calculate_dutiable_value_by_air(), 1286440.0)


if __name__ == '__main__':
    unittest.main()
