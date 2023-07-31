
class ACBulkBreakBulkCargo:
    def __init__(self, type_of_cargo: float, total_mt_or_rt: float) -> None:
        self.type_of_cargo = type_of_cargo
        self.total_mt_or_rt = total_mt_or_rt
        self.ac_rate = float
        self.general_cargo = 1
        self.bagged_cargo = 2
        self.palletized = 3
        self.unpacked_fish = 4
        self.fish_in_cartons = 5
        self.steel_products = 6
        self.logs = 7
        self.lumber = 8
        self.heavy_lift_5to15_tons = 9
        self.heavy_lift_over15to20_tons = 10
        self.heavy_lift_over20_tons = 11
        self.checking_charge_shipside = 12

    def calculate_bulk_break_bulk_cargo(self, ac_rate: float) -> float:
        total_ac = round(
            self.total_mt_or_rt * ac_rate, 2
        )
        return total_ac


class ACBulkBreakBulkCargoImport(ACBulkBreakBulkCargo):
    def __init__(self, type_of_cargo: float, total_mt_or_rt: float) -> None:
        super().__init__(type_of_cargo, total_mt_or_rt)
        self.general_cargo_rate = 149.00
        self.bagged_cargo_rate = 264.00
        self.palletized_rate = 117.00
        self.unpacked_fish_rate = 994.00
        self.fish_in_cartons_rate = 664.00
        self.steel_products_rate = 175.00
        self.logs_rate = 228.00,
        self.lumber_rate = 228.00
        self.heavy_lift_5to15_tons_rate = 359.00
        self.heavy_lift_over15to20_tons_rate = 593.00
        self.heavy_lift_over20_tons_rate = 835.00
        self.checking_charge_shipside_rate = 17.00

    def calculate_lcl_import(self) -> float:
        if self.type_of_cargo == self.general_cargo:
            self.ac_rate = self.general_cargo_rate

        elif self.type_of_cargo == self.bagged_cargo:
            self.ac_rate = self.bagged_cargo_rate

        elif self.type_of_cargo == self.palletized:
            self.ac_rate = self.palletized_rate

        elif self.type_of_cargo == self.unpacked_fish:
            self.ac_rate = self.unpacked_fish_rate

        elif self.type_of_cargo == self.fish_in_cartons:
            self.ac_rate = self.fish_in_cartons_rate

        elif self.type_of_cargo == self.steel_products:
            self.ac_rate = self.steel_products_rate

        elif self.type_of_cargo == self.logs:
            self.ac_rate = self.logs_rate

        elif self.type_of_cargo == self.lumber:
            self.ac_rate = self.lumber_rate

        elif self.type_of_cargo == self.heavy_lift_5to15_tons:
            self.ac_rate = self.heavy_lift_5to15_tons_rate

        elif self.type_of_cargo == self.heavy_lift_over15to20_tons:
            self.ac_rate = self.heavy_lift_over15to20_tons_rate

        elif self.type_of_cargo == self.heavy_lift_over20_tons:
            self.ac_rate = self.heavy_lift_over20_tons_rate

        elif self.type_of_cargo == self.checking_charge_shipside:
            self.ac_rate = self.checking_charge_shipside_rate

        return self.calculate_bulk_break_bulk_cargo(self.ac_rate)


class ACBulkBreakBulkCargoExport(ACBulkBreakBulkCargo):
    def __init__(self, type_of_cargo: float, total_mt_or_rt: float) -> None:
        super().__init__(type_of_cargo, total_mt_or_rt)
        self.general_cargo_rate = 122.00
        self.bagged_cargo_rate = 216.00
        self.palletized_rate = 96.00
        self.unpacked_fish_rate = 812.00
        self.fish_in_cartons_rate = 542.00
        self.steel_products_rate = 143.00
        self.logs_rate = 186.00
        self.lumber_rate = 186.00
        self.heavy_lift_5to15_tons_rate = 293.00
        self.heavy_lift_over15to20_tons_rate = 484.00
        self.heavy_lift_over20_tons_rate = 682.00
        self.checking_charge_shipside_rate = 17.00

    def calculate_lcl_export(self) -> float:
        if self.type_of_cargo == self.general_cargo:
            self.ac_rate = self.general_cargo_rate

        elif self.type_of_cargo == self.bagged_cargo:
            self.ac_rate = self.bagged_cargo_rate

        elif self.type_of_cargo == self.palletized:
            self.ac_rate = self.palletized_rate

        elif self.type_of_cargo == self.unpacked_fish:
            self.ac_rate = self.unpacked_fish_rate

        elif self.type_of_cargo == self.fish_in_cartons:
            self.ac_rate = self.fish_in_cartons_rate

        elif self.type_of_cargo == self.steel_products:
            self.ac_rate = self.steel_products_rate

        elif self.type_of_cargo == self.logs:
            self.ac_rate = self.logs_rate

        elif self.type_of_cargo == self.lumber:
            self.ac_rate = self.lumber_rate

        elif self.type_of_cargo == self.heavy_lift_5to15_tons:
            self.ac_rate = self.heavy_lift_5to15_tons_rate

        elif self.type_of_cargo == self.heavy_lift_over15to20_tons:
            self.ac_rate = self.heavy_lift_over15to20_tons_rate

        elif self.type_of_cargo == self.heavy_lift_over20_tons:
            self.ac_rate = self.heavy_lift_over20_tons_rate

        elif self.type_of_cargo == self.checking_charge_shipside:
            self.ac_rate = self.checking_charge_shipside_rate

        return self.calculate_bulk_break_bulk_cargo(self.ac_rate)
