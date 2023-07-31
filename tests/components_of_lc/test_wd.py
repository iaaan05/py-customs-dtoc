import unittest
from customs_dtoc import WDOutportsViaShipside, WDOutportsViaPierside, WDContainerizedCargoImport, \
    WDContainerizedCargoExport, WDBulkBreakBulkCargoImport, WDBulkBreakBulkCargoExport, \
    WDContainerizedDangerousCargo20Footer, WDContainerizedDangerousCargo40Footer


class TestWharfageDue(unittest.TestCase):
    def test_wd_outport_shipside(self):
        wd_outport_shipside = WDOutportsViaShipside(
            total_mt=100
        )
        self.assertEqual(
            wd_outport_shipside.calculate_wd_outport_via_shipside(), 1700.0
        )

    def test_wd_outport_pierside(self):
        wd_outport_pierside = WDOutportsViaPierside(
            total_mt=100
        )
        self.assertEqual(
            wd_outport_pierside.calculate_wd_outport_via_pierside(), 3400.0
        )

    def test_wd_fcl_import(self):
        wd_fcl_import = WDContainerizedCargoImport(
            size_of_container=20, total_number_of_containers=4
        )
        self.assertEqual(wd_fcl_import.calculate_fcl_import(), 2077.40)

    def test_wd_fcl_export(self):
        wd_fcl_export = WDContainerizedCargoExport(
            size_of_container=20, total_number_of_containers=4
        )
        self.assertEqual(wd_fcl_export.calculate_fcl_export(), 1038.80)

    def test_wd_lcl_import(self):
        wd_lcl_import = WDBulkBreakBulkCargoImport(
            type_of_ton=1, total_mt_or_rt=50
        )
        self.assertEqual(wd_lcl_import.calculate_lcl_import(), 1527.50)

    def test_wd_lcl_export(self):
        wd_lcl_export = WDBulkBreakBulkCargoExport(
            type_of_ton=1, total_mt_or_rt=50
        )
        self.assertEqual(wd_lcl_export.calculate_lcl_export(), 762.50)

    def test_wd_containerized_dangerous_cargo_20_footer(self):
        wd_containerized_dangerous_cargo_20_footer = WDContainerizedDangerousCargo20Footer(
            total_number_of_containers=4
        )
        self.assertEqual(
            wd_containerized_dangerous_cargo_20_footer.calculate_containerized_dangerous_cargo_20_footer(), 2077.40
        )

    def test_wd_containerized_dangerous_cargo_40_footer(self):
        wd_containerized_dangerous_cargo_40_footer = WDContainerizedDangerousCargo40Footer(
            total_number_of_containers=4
        )
        self.assertEqual(
            wd_containerized_dangerous_cargo_40_footer.calculate_containerized_dangerous_cargo_40_footer(), 3116.20
        )


if __name__ == '__main__':
    unittest.main()
