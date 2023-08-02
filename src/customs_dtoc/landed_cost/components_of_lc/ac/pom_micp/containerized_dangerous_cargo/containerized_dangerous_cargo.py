import json
import os


def get_rate_for_dangerous_cargo(class_dangerous_cargo: str, file_name: str) -> float:
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        rates = json.load(f)
    return rates.get(class_dangerous_cargo, 0.0)


class ContainerizedDangerousCargoClass:
    CLASS_DANGEROUS_CARGO = {
        1.0: 'Class 1, 6, and 8', 2.0: 'Class 2, 3, 4, and 7', 3.0: 'Class 5 and 9'
    }

    def __init__(self, classification_of_dangerous_cargo: float, total_number_of_containers: float) -> None:
        self.class_dangerous_cargo = classification_of_dangerous_cargo
        self.total_number_of_containers = total_number_of_containers
        self.ac_rate = float

    def calculate_fcl_footer(self, ac_rate) -> float:
        total_ac = round(
            self.total_number_of_containers * ac_rate, 2
        )
        return total_ac


class ACContainerizedDangerousCargo20Footer(ContainerizedDangerousCargoClass):
    def calculate_fcl_20_footer(self) -> float:
        class_dangerous_cargo = ContainerizedDangerousCargoClass.CLASS_DANGEROUS_CARGO[self.class_dangerous_cargo]
        self.ac_rate = get_rate_for_dangerous_cargo(class_dangerous_cargo, '20_footer_rates.json')
        return self.calculate_fcl_footer(self.ac_rate)


class ACContainerizedDangerousCargo40Footer(ContainerizedDangerousCargoClass):
    def calculate_fcl_40_footer(self) -> float:
        class_dangerous_cargo = ContainerizedDangerousCargoClass.CLASS_DANGEROUS_CARGO[self.class_dangerous_cargo]
        self.ac_rate = get_rate_for_dangerous_cargo(class_dangerous_cargo, '40_footer_rates.json')
        return self.calculate_fcl_footer(self.ac_rate)
