import json
import os


def get_rate_of_ton_type(ton_type: str, file_name: str) -> float:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        rates = json.load(f)
    return rates.get(ton_type, 0.0)


class WDBulkBreakBulkCargo:
    TON_TYPES = {1.0: 'Revenue Ton', 2.0: 'Metric Ton'}

    def __init__(self, type_of_ton: float, total_mt_or_rt: float) -> None:
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt
        self.wd_rate = float

    def calculate_lcl(self, wd_rate) -> float:
        total_wd = round(
            self.total_mt_or_rt * wd_rate, 2
        )
        return total_wd


class WDBulkBreakBulkCargoImport(WDBulkBreakBulkCargo):
    def calculate_lcl_import(self) -> float:
        ton_type = WDBulkBreakBulkCargo.TON_TYPES[self.type_of_ton]
        self.wd_rate = get_rate_of_ton_type(ton_type, 'import_rates.json')
        return self.calculate_lcl(self.wd_rate)


class WDBulkBreakBulkCargoExport(WDBulkBreakBulkCargo):
    def calculate_lcl_export(self) -> float:
        ton_type = WDBulkBreakBulkCargo.TON_TYPES[self.type_of_ton]
        self.wd_rate = get_rate_of_ton_type(ton_type, 'export_rates.json')
        return self.calculate_lcl(self.wd_rate)
