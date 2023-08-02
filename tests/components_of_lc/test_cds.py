import unittest
from customs_dtoc import CustomsDocumentaryStamp


class TestCustomsDocumentaryStamp(unittest.TestCase):
    def test_cds_formal(self):
        cds_formal = CustomsDocumentaryStamp(type_of_entry=1)
        self.assertEqual(cds_formal.calculate_cds(), 280.0)

    def test_cds_informal(self):
        cds_informal = CustomsDocumentaryStamp(type_of_entry=2)
        self.assertEqual(cds_informal.calculate_cds(), 30.0)


if __name__ == '__main__':
    unittest.main()
