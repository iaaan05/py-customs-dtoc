import unittest
from customs_dtoc import VatExciseTax, VatNonExciseTax


class TestValueAddedTax(unittest.TestCase):
    def test_vat_with_excise_tax(self):
        vat_with_et = VatExciseTax(landed_cost=12584351.12, excise_tax=10200)
        self.assertEqual(vat_with_et.calculate_vat_with_et(), 1511346.13)

    def test_vat_non_excise_tax(self):
        vat_non_et = VatNonExciseTax(landed_cost=12584351.12)
        self.assertEqual(vat_non_et.calculate_vat_non_excise_tax(), 1510122.13)


if __name__ == '__main__':
    unittest.main()
