import json
import os


def get_rate_of_container_size(container_size: str, file_name: str) -> float:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        rates = json.load(f)
    return rates.get(container_size, 0.0)


class WDContainerizedCargo:
    CONTAINER_SIZE = {
        20.0: 'Twenty Footer', 40.0: 'Forty Footer', 45.0: 'Forty-Five Footer'
    }

    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.total_number_of_containers = total_number_of_containers
        self.wd_rate = float

    def calculate_fcl(self, wd_rate) -> float:
        total_wd = round(
            self.total_number_of_containers * wd_rate, 2
        )
        return total_wd


class WDContainerizedCargoImport(WDContainerizedCargo):
    def calculate_fcl_import(self):
        container_size = WDContainerizedCargo.CONTAINER_SIZE[self.size_of_container]
        self.wd_rate = get_rate_of_container_size(container_size, 'import_rates.json')
        return self.calculate_fcl(self.wd_rate)


class WDContainerizedCargoExport(WDContainerizedCargo):
    def calculate_fcl_export(self):
        container_size = WDContainerizedCargo.CONTAINER_SIZE[self.size_of_container]
        self.wd_rate = get_rate_of_container_size(container_size, 'export_rates.json')
        return self.calculate_fcl(self.wd_rate)
