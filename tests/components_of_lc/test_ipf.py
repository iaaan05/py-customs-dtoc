import unittest
from customs_dtoc import ImportProcessingFee


class TestImportProcessingFee(unittest.TestCase):
    def test_ipf(self):
        ipf = ImportProcessingFee(dutiable_value=2145621.31)
        self.assertEqual(ipf.calculate_dv_to_ipf(), 1000.0)


if __name__ == '__main__':
    unittest.main()
