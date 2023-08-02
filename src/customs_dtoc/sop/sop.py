
import math


class SummaryOfPaymentsWithLetterOfCredit:
    def __init__(self, customs_duty: float, value_added_tax: float, excise_tax: float, import_processing_fee: float,
                 customs_documentary_stamps: float, container_security_fee: float, advance_deposit: float) -> None:
        self.customs_duty = customs_duty
        self.value_added_tax = value_added_tax
        self.excise_tax = excise_tax
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps
        self.container_security_fee = container_security_fee
        self.advance_deposit = advance_deposit

    def calculate_sop_with_letter_of_credit(self) -> float:
        total_duties_taxes_other_charges = (
            self.customs_duty, self.value_added_tax, self.excise_tax, self.import_processing_fee,
            self.customs_documentary_stamps, self.container_security_fee
        )
        total_net_amount_payable = round(math.fsum(total_duties_taxes_other_charges) - self.advance_deposit, 2)
        return total_net_amount_payable


class SummaryOfPaymentsNonLetterOfCredit:
    def __init__(self, customs_duty: float, value_added_tax: float, excise_tax: float, import_processing_fee: float,
                 customs_documentary_stamps: float, container_security_fee: float) -> None:
        self.customs_duty = customs_duty
        self.value_added_tax = value_added_tax
        self.excise_tax = excise_tax
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps
        self.container_security_fee = container_security_fee

    def calculate_sop_non_letter_of_credit(self) -> float:
        total_duties_taxes_other_charges = (
            self.customs_duty, self.value_added_tax, self.excise_tax, self.import_processing_fee,
            self.customs_documentary_stamps, self.container_security_fee
        )
        total_customs_duties_taxes_other_charges = round(math.fsum(total_duties_taxes_other_charges), 2)
        return total_customs_duties_taxes_other_charges


class SummaryOfPaymentsWithInformalEntry:
    def __init__(self, customs_duty: float, value_added_tax: float, excise_tax: float,
                 customs_documentary_stamps: float) -> None:
        self.customs_duty = customs_duty
        self.value_added_tax = value_added_tax
        self.excise_tax = excise_tax
        self.customs_documentary_stamps = customs_documentary_stamps

    def calculate_sop_with_informal_entry(self) -> float:
        total_duties_taxes_other_charges = (
            self.customs_duty, self.value_added_tax, self.excise_tax, self.customs_documentary_stamps,
        )
        total_duties_taxes_other_charges = round(math.fsum(total_duties_taxes_other_charges), 2)
        return total_duties_taxes_other_charges
