import unittest
from customs_dtoc import ProRataIndividualFreight, ProRataIndividualInsurance, ProRataIndividualDutiableValue, \
    ProRataIndividualMiscExpenses


class TestProRataIndividual(unittest.TestCase):
    def test_pro_rata_individual_freight(self):
        pro_rata_individual_frt = ProRataIndividualFreight(
            individual_fob=3614.54, total_fob=14548.64, total_frt=3000
        )
        self.assertEqual(
            pro_rata_individual_frt.calculate_pro_rata_individual_freight(), 745.34
        )

    def test_pro_rata_individual_insurance(self):
        pro_rata_individual_ins = ProRataIndividualInsurance(
            individual_fob=3614.54, total_fob=14548.64, total_ins=5000
        )
        self.assertEqual(
            pro_rata_individual_ins.calculate_pro_rata_individual_insurance(), 1242.23
        )

    def test_pro_rata_individual_dutiable_value(self):
        pro_rata_individual_dv = ProRataIndividualDutiableValue(
            individual_fob=3614.54, total_fob=14548.64, total_dutiable_value=1648254.13
        )
        self.assertEqual(
            pro_rata_individual_dv.calculate_pro_rata_individual_dutiable_value(), 409500.85
        )

    def test_pro_rata_individual_miscellaneous_expenses(self):
        pro_rata_individual_me = ProRataIndividualMiscExpenses(
            individual_fob=3614.54, total_fob=14548.64, total_misc_expenses=8542.58
        )
        self.assertEqual(
            pro_rata_individual_me.calculate_pro_rata_individual_misc_expenses(), 2122.36
        )


if __name__ == '__main__':
    unittest.main()
