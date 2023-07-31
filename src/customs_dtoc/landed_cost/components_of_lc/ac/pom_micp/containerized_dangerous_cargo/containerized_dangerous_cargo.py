class ContainerizedDangerousCargoClass:
    def __init__(self, classification_of_dangerous_cargo: float, total_number_of_containers: float) -> None:
        self.classification_of_dangerous_cargo = classification_of_dangerous_cargo
        self.total_number_of_containers = total_number_of_containers
        self.ac_rate = float
        self.class_1_6_8 = 1
        self.class_2_3_4_7 = 2
        self.class_5_9 = 3

    def calculate_fcl_footer(self, ac_rate) -> float:
        total_ac = round(
            self.total_number_of_containers * ac_rate, 2
        )
        return total_ac


class ACContainerizedDangerousCargo20Footer(ContainerizedDangerousCargoClass):
    def __init__(self, classification_of_dangerous_cargo: float, total_number_of_containers: float) -> None:
        super().__init__(classification_of_dangerous_cargo, total_number_of_containers)
        self.class_1_6_8_rate = 5590.50
        self.class_2_3_4_7_rate = 4658.75
        self.class_5_9_rate = 4099.70

    def calculate_fcl_20_footer(self) -> float:
        if self.classification_of_dangerous_cargo == self.class_1_6_8:
            self.ac_rate = self.class_1_6_8_rate

        elif self.classification_of_dangerous_cargo == self.class_2_3_4_7:
            self.ac_rate = self.class_2_3_4_7_rate

        elif self.classification_of_dangerous_cargo == self.class_5_9:
            self.ac_rate = self.class_5_9_rate

        return self.calculate_fcl_footer(self.ac_rate)


class ACContainerizedDangerousCargo40Footer(ContainerizedDangerousCargoClass):
    def __init__(self, classification_of_dangerous_cargo: float, total_number_of_containers: float) -> None:
        super().__init__(classification_of_dangerous_cargo, total_number_of_containers)
        self.class_1_6_8_rate = 12826.00
        self.class_2_3_4_7_rate = 10688.75
        self.class_5_9_rate = 9406.10

    def calculate_fcl_40_footer(self) -> float:
        if self.classification_of_dangerous_cargo == self.class_1_6_8:
            self.ac_rate = self.class_1_6_8_rate

        elif self.classification_of_dangerous_cargo == self.class_2_3_4_7:
            self.ac_rate = self.class_2_3_4_7_rate

        elif self.classification_of_dangerous_cargo == self.class_5_9:
            self.ac_rate = self.class_5_9_rate

        return self.calculate_fcl_footer(self.ac_rate)
