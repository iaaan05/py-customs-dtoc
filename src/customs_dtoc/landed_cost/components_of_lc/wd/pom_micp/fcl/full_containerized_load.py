class WDContainerizedCargo:
    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.total_number_of_containers = total_number_of_containers
        self.twenty_footer = 20
        self.forty_footer = 40
        self.forty_five_footer = 45

    def calculate_fcl(self, wd_rate) -> float:
        total_wd = round(
            self.total_number_of_containers * wd_rate, 2
        )
        return total_wd


class WDContainerizedCargoImport(WDContainerizedCargo):
    def __init__(self, size_of_container, total_number_of_containers) -> None:
        super().__init__(size_of_container, total_number_of_containers)
        self.wd_rate = float
        self.twenty_footer_rate = 519.35
        self.forty_footer_rate = 779.05
        self.forty_five_footer_rate = 916.50

    def calculate_fcl_import(self):
        if self.size_of_container == self.twenty_footer:
            self.wd_rate = self.twenty_footer_rate

        elif self.size_of_container == self.forty_footer:
            self.wd_rate = self.forty_footer_rate

        elif self.size_of_container == self.forty_five_footer:
            self.wd_rate = self.forty_five_footer_rate

        return self.calculate_fcl(self.wd_rate)


class WDContainerizedCargoExport(WDContainerizedCargo):
    def __init__(self, size_of_container, total_number_of_containers) -> None:
        super().__init__(size_of_container, total_number_of_containers)
        self.wd_rate = float
        self.twenty_footer_rate = 259.70
        self.forty_footer_rate = 391.05
        self.forty_five_footer_rate = 458.25

    def calculate_fcl_export(self):
        if self.size_of_container == self.twenty_footer:
            self.wd_rate = self.twenty_footer_rate

        elif self.size_of_container == self.forty_footer:
            self.wd_rate = self.forty_footer_rate

        elif self.size_of_container == self.forty_five_footer:
            self.wd_rate = self.forty_five_footer_rate

        return self.calculate_fcl(self.wd_rate)
