import unittest
from customs_dtoc import BrokerageFeeFormalEntry


class TestBrokerageFee(unittest.TestCase):
    def test_bf_formal_entry(self):
        bf_formal_entry = BrokerageFeeFormalEntry(
            dutiable_value=2145621.31
        )
        self.assertEqual(bf_formal_entry.calculate_dv_to_bf_formal(), 7732.03)


if __name__ == '__main__':
    unittest.main()
