import json
import os


def get_rate_for_container_size(container_size: str, file_name: str) -> float:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        rates = json.load(f)
    return rates.get(container_size, 0.0)


class ACContainerizedCargo:
    CONTAINER_SIZE = {
        20.0: 'Twenty Footer', 40.0: 'Forty Footer', 45.0: 'Forty-Five Footer'
    }

    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.total_number_of_containers = total_number_of_containers
        self.ac_rate = float

    def calculate_containerized_cargo(self, ac_rate: float) -> float:
        total_ac = round(
            self.total_number_of_containers * ac_rate, 2
        )
        return total_ac


class ACContainerizedCargoImport(ACContainerizedCargo):
    def calculate_fcl_import(self) -> float:
        container_size = ACContainerizedCargo.CONTAINER_SIZE[self.size_of_container]
        self.ac_rate = get_rate_for_container_size(container_size, 'import_rates.json')
        return self.calculate_containerized_cargo(self.ac_rate)


class ACContainerizedCargoExport(ACContainerizedCargo):
    def calculate_fcl_export(self) -> float:
        container_size = ACContainerizedCargo.CONTAINER_SIZE[self.size_of_container]
        self.ac_rate = get_rate_for_container_size(container_size, 'export_rates.json')
        return self.calculate_containerized_cargo(self.ac_rate)


class ACContainerizedCargoShutOutExport:
    CONTAINER_TYPES = {
        1.0: 'Full or Loaded Container', 2.0: 'Empty Container'
    }

    def __init__(self, total_number_of_containers: float, type_of_container: float) -> None:
        self.total_number_of_containers = total_number_of_containers
        self.type_of_container = type_of_container
        self.ac_rate = float

    def calculate_fcl_shutout_export(self) -> float:
        container_type = ACContainerizedCargoShutOutExport.CONTAINER_TYPES[self.type_of_container]
        self.ac_rate = get_rate_for_container_size(container_type, 'shutout_export_rates.json')
        total_ac = round(
            self.total_number_of_containers * self.ac_rate, 2
        )
        return total_ac
