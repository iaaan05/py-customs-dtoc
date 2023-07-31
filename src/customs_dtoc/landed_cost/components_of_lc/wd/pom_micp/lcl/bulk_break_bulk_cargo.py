class WDBulkBreakBulkCargo:
    def __init__(self, type_of_ton: float, total_mt_or_rt: float) -> None:
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt
        self.wd_rate = float
        self.rt_type = 1
        self.mt_type = 2

    def calculate_lcl(self, wd_rate) -> float:
        total_wd = round(
            self.total_mt_or_rt * wd_rate, 2
        )
        return total_wd


class WDBulkBreakBulkCargoImport(WDBulkBreakBulkCargo):
    def __init__(self, type_of_ton, total_mt_or_rt) -> None:
        super().__init__(type_of_ton, total_mt_or_rt)
        self.rt = 30.55
        self.mt = 36.65

    def calculate_lcl_import(self) -> float:
        if self.type_of_ton == self.rt_type:
            self.wd_rate = self.rt

        elif self.type_of_ton == self.mt_type:
            self.wd_rate = self.mt

        return self.calculate_lcl(self.wd_rate)


class WDBulkBreakBulkCargoExport(WDBulkBreakBulkCargo):
    def __init__(self, type_of_ton, total_mt_or_rt) -> None:
        super().__init__(type_of_ton, total_mt_or_rt)
        self.rt = 15.25
        self.mt = 18.35

    def calculate_lcl_export(self) -> float:
        if self.type_of_ton == self.rt_type:
            self.wd_rate = self.rt

        elif self.type_of_ton == self.mt_type:
            self.wd_rate = self.mt

        return self.calculate_lcl(self.wd_rate)
