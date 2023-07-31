import unittest
from customs_dtoc import ACOutportsViaShipside, ACOutportsViaPierside, \
    ACContainerizedCargoImport, ACContainerizedCargoExport, ACContainerizedCargoShutOutExport, \
    ACBulkBreakBulkCargoImport, ACBulkBreakBulkCargoExport, ACContainerizedDangerousCargo20Footer, \
    ACContainerizedDangerousCargo40Footer


class TestArrastreCharge(unittest.TestCase):
    def test_ac_outport_shipside(self):
        ac_outport_shipside = ACOutportsViaShipside(
            total_metric_ton=100
        )
        self.assertEqual(ac_outport_shipside.calculate_ac_outport_via_shipside(), 800.0)

    def test_ac_outport_pierside(self):
        ac_outport_pierside = ACOutportsViaPierside(
            total_metric_ton=100
        )
        self.assertEqual(ac_outport_pierside.calculate_ac_outport_via_pierside(), 11000.0)

    def test_ac_fcl_import(self):
        ac_fcl_import = ACContainerizedCargoImport(
            size_of_container=20, total_number_of_containers=4
        )
        self.assertEqual(ac_fcl_import.calculate_fcl_import(), 14908.0)

    def test_ac_fcl_export(self):
        ac_fcl_export = ACContainerizedCargoExport(
            size_of_container=20, total_number_of_containers=4
        )
        self.assertEqual(ac_fcl_export.calculate_fcl_export(), 12172.0)

    def test_ac_fcl_shut_out_export(self):
        ac_fcl_shut_out_export = ACContainerizedCargoShutOutExport(
            total_number_of_containers=4, type_of_shutout_export_container=1
        )
        self.assertEqual(ac_fcl_shut_out_export.calculate_fcl_shutout_export(), 12156.0)

    def test_ac_lcl_import(self):
        ac_lcl_import = ACBulkBreakBulkCargoImport(
            type_of_cargo=1, total_mt_or_rt=50
        )
        self.assertEqual(ac_lcl_import.calculate_lcl_import(), 7450.0)

    def test_ac_lcl_export(self):
        ac_lcl_export = ACBulkBreakBulkCargoExport(
            type_of_cargo=1, total_mt_or_rt=50
        )
        self.assertEqual(ac_lcl_export.calculate_lcl_export(), 6100.0)

    def test_ac_containerized_dangerous_cargo_20_footer(self):
        ac_containerized_dangerous_cargo_20_footer = ACContainerizedDangerousCargo20Footer(
            classification_of_dangerous_cargo=1, total_number_of_containers=4
        )
        self.assertEqual(ac_containerized_dangerous_cargo_20_footer.calculate_fcl_20_footer(), 22362.0)

    def test_ac_containerized_dangerous_cargo_40_footer(self):
        ac_containerized_dangerous_cargo_40_footer = ACContainerizedDangerousCargo40Footer(
            classification_of_dangerous_cargo=1, total_number_of_containers=4
        )
        self.assertEqual(ac_containerized_dangerous_cargo_40_footer.calculate_fcl_40_footer(), 51304.0)


if __name__ == '__main__':
    unittest.main()
