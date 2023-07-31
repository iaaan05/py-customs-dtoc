class CustomsDocumentaryStamp:
    def __init__(self, type_of_entry: float) -> None:
        self.type_of_entry = type_of_entry
        self.formal_entry = 1
        self.informal_entry = 2

    def calculate_cds(self):
        if self.type_of_entry == self.formal_entry:
            cds = 280.00
            return cds

        elif self.type_of_entry == self.informal_entry:
            cds = 30.00
            return cds
