class ContainerSecurityFee:
    def __init__(self, number_of_containers: float, rate_of_exchange: float) -> None:
        self.number_of_containers = number_of_containers
        self.rate_of_exchange = rate_of_exchange

    def calculate_csf(self, container_security_fee_rate: float) -> float:
        total_security_fee = round(
            self.number_of_containers * container_security_fee_rate * self.rate_of_exchange, 2
        )
        return total_security_fee


class CSF20Footer(ContainerSecurityFee):
    def __init__(self, number_of_containers: float, rate_of_exchange: float) -> None:
        super().__init__(number_of_containers, rate_of_exchange)
        self.container_security_fee_rate = 5.00

    def calculate_csf_20_footer(self) -> float:
        return self.calculate_csf(self.container_security_fee_rate)


class CSF40Footer(ContainerSecurityFee):
    def __init__(self, number_of_containers: float, rate_of_exchange: float) -> None:
        super().__init__(number_of_containers, rate_of_exchange)
        self.container_security_fee_rate = 10.00

    def calculate_csf_40_footer(self) -> float:
        return self.calculate_csf(self.container_security_fee_rate)
