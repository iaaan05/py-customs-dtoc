import unittest
from customs_dtoc import SummaryOfPaymentsWithLetterOfCredit, SummaryOfPaymentsNonLetterOfCredit, \
    SummaryOfPaymentsWithInformalEntry


class TestSummaryOfPayments(unittest.TestCase):
    def test_sop_with_letter_of_credit(self):
        sop_with_letter_of_credit = SummaryOfPaymentsWithLetterOfCredit(
            customs_duty=24658.43, value_added_tax=32213.41, excise_tax=14586.12, import_processing_fee=1000,
            customs_documentary_stamps=280, container_security_fee=3582.10, advance_deposit=25000
        )
        self.assertEqual(sop_with_letter_of_credit.calculate_sop_with_letter_of_credit(), 51320.06)

    def test_sop_non_letter_of_credit(self):
        sop_non_letter_of_credit = SummaryOfPaymentsNonLetterOfCredit(
            customs_duty=24658.43, value_added_tax=32213.41, excise_tax=14586.12, import_processing_fee=1000,
            customs_documentary_stamps=280, container_security_fee=3582.10
        )
        self.assertEqual(sop_non_letter_of_credit.calculate_sop_non_letter_of_credit(), 76320.06)

    def test_sop_with_informal_entry(self):
        sop_with_informal_entry = SummaryOfPaymentsWithInformalEntry(
            customs_duty=24658.43, value_added_tax=32213.41, excise_tax=14586.12, customs_documentary_stamps=280
        )
        self.assertEqual(sop_with_informal_entry.calculate_sop_with_informal_entry(), 71737.96)


if __name__ == '__main__':
    unittest.main()
