import unittest
from customs_dtoc import BankCharge


class TestBankCharge(unittest.TestCase):
    def test_bank_charge(self):
        bank_charge = BankCharge(
            dutiable_value=2145621.31
        )
        self.assertEqual(bank_charge.calculate_bc(), 2682.03)


if __name__ == '__main__':
    unittest.main()
