import unittest
from customs_dtoc import CSF20Footer, CSF40Footer


class TestContainerSecurityFee(unittest.TestCase):
    def test_csf_20_footer(self):
        csf_20_footer = CSF20Footer(number_of_containers=10, rate_of_exchange=55.45)
        self.assertEqual(csf_20_footer.calculate_csf_20_footer(), 2772.50)

    def test_csf_40_footer(self):
        csf_40_footer = CSF40Footer(number_of_containers=10, rate_of_exchange=55.45)
        self.assertEqual(csf_40_footer.calculate_csf_40_footer(), 5545.0)


if __name__ == '__main__':
    unittest.main()
