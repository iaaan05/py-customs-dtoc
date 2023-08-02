import json
import os


def get_rate_for_cargo(cargo_type: str, file_name: str) -> float:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        rates = json.load(f)
    return rates.get(cargo_type, 0.0)


class ACBulkBreakBulkCargo:
    CARGO_TYPES = {
        1: 'General Cargo', 2: 'Bagged Cargo', 3: 'Palletized', 4: 'Unpacked Fish', 5: 'Fish in Cartons',
        6: 'Steel Products', 7: 'Logs', 8: 'Lumber', 9: 'Heavy lift over 5 to 15 Tons',
        10: 'Heavy lift over 15 to 20 Tons', 11: 'Heavy lift over 20 Tons', 12: 'Checking Charge Shipside'}

    def __init__(self, type_of_cargo: float, total_mt_or_rt: float) -> None:
        self.type_of_cargo = type_of_cargo
        self.total_mt_or_rt = total_mt_or_rt
        self.ac_rate = float

    def calculate_bulk_break_bulk_cargo(self, ac_rate: float) -> float:
        total_ac = round(
            self.total_mt_or_rt * ac_rate, 2
        )
        return total_ac


class ACBulkBreakBulkCargoImport(ACBulkBreakBulkCargo):
    def calculate_lcl_import(self) -> float:
        cargo_type = ACBulkBreakBulkCargo.CARGO_TYPES[self.type_of_cargo]
        self.ac_rate = get_rate_for_cargo(cargo_type, 'import_rates.json')
        return self.calculate_bulk_break_bulk_cargo(self.ac_rate)


class ACBulkBreakBulkCargoExport(ACBulkBreakBulkCargo):
    def calculate_lcl_export(self) -> float:
        cargo_type = ACBulkBreakBulkCargo.CARGO_TYPES[self.type_of_cargo]
        self.ac_rate = get_rate_for_cargo(cargo_type, 'export_rates.json')
        return self.calculate_bulk_break_bulk_cargo(self.ac_rate)
