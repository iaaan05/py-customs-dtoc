class ImportProcessingFee:
    def __init__(self, dutiable_value: float) -> None:
        self.dutiable_value = dutiable_value
        self.ipf_250 = 250.00
        self.ipf_500 = 500.00
        self.ipf_750 = 750.00
        self.ipf_1000 = 1000.00

    def calculate_dv_to_ipf(self) -> float:
        if self.dutiable_value <= 250000:
            import_processing_fee = self.ipf_250
            return import_processing_fee

        elif 250000 < self.dutiable_value <= 500000:
            import_processing_fee = self.ipf_500
            return import_processing_fee

        elif 500000 < self.dutiable_value <= 750000:
            import_processing_fee = self.ipf_750
            return import_processing_fee

        elif self.dutiable_value > 750000:
            import_processing_fee = self.ipf_1000
            return import_processing_fee
