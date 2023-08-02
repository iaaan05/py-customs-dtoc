class CustomsDocumentaryStamp:
    ENTRY_TYPES = {1.0: 'Formal Entry', 2.0: 'Informal Entry'}

    def __init__(self, type_of_entry: float) -> None:
        self.type_of_entry = type_of_entry
        self.cds = float

    def calculate_cds(self) -> float:
        entry_type = CustomsDocumentaryStamp.ENTRY_TYPES[self.type_of_entry]
        if entry_type == 'Formal Entry':
            self.cds = 280.0
            return self.cds

        elif entry_type == 'Informal Entry':
            self.cds = 30.0
            return self.cds
