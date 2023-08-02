import unittest
from customs_dtoc import CustomsDuty


class TestCustomsDuty(unittest.TestCase):
    def test_cud(self):
        cud = CustomsDuty(
            dutiable_value=2145621.31, rate_of_duty=15
        )
        self.assertEqual(cud.calculate_cud(), 321843.20)


if __name__ == '__main__':
    unittest.main()
