class WDContainerizedDangerousCargo:
    def __init__(self, total_number_of_containers: float):
        self.total_number_of_containers = total_number_of_containers

    def calculate_fcl_footer(self, container_footer_rate):
        total_wd = round(
            self.total_number_of_containers * container_footer_rate, 2
        )
        return total_wd


class WDContainerizedDangerousCargo20Footer(WDContainerizedDangerousCargo):
    def __init__(self, total_number_of_containers) -> None:
        super().__init__(total_number_of_containers)
        self.container_footer_rate = 519.35

    def calculate_containerized_dangerous_cargo_20_footer(self) -> float:
        return self.calculate_fcl_footer(self.container_footer_rate)


class WDContainerizedDangerousCargo40Footer(WDContainerizedDangerousCargo):
    def __init__(self, total_number_of_containers) -> None:
        super().__init__(total_number_of_containers)
        self.container_footer_rate = 779.05

    def calculate_containerized_dangerous_cargo_40_footer(self) -> float:
        return self.calculate_fcl_footer(self.container_footer_rate)
