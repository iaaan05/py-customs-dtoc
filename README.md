# Customs Formula: Duties, Taxes, and Other Charges

## INTRODUCTION:
This is a `Python package` that I personally made to compute the customs duties, taxes, and other charges. A sample 
Command-Line Interface (CLI) calculator project using this package will be posted on my GitHub repo soon. Further 
improvements will be made on this.

## NOTES:
These are the duties, taxes, and other charges that will be computed by using this package: 

Note: The package is still incomplete since it does not handle the situations where there are missing components and 
the backward computation of each computation.

### Total Landed Cost 
  - Formal Entry
    - Sea
    - Air
  - Informal Entry
    - Sea/Air


### Components of Landed Cost
  - **Dutiable Value** (DV)
    - Sea
    - Air
  - **Customs Duty** (CUD)
  - **Bank Charge** (BC)
  - **Brokerage Fee** (B/F)
    - Formal Entry
  - **Arrastre Charge** (A/C)
    - Outports
      - Shipside
      - Pierside
    - Port of Manila (POM) and Manila International Container Port (MICP)
      - Containerized Cargo (FCL)
        - Import
        - Export
        - Shut-out Export
      - Bulk or Break-bulk Cargo (LCL)
        - Import
        - Export
      - Containerized Dangerous Cargo
        - Class 1, 6, and 8
        - Class 2, 3, 4, and 7
        - Class 5 and 9
  - **Wharfage Due** (W/D)
    - Outports
      - Shipside
      - Pierside
    - Port of Manila (POM) and Manila International Container Port (MICP)
      - Containerized Cargo (FCL)
        - Import
        - Export
      - Bulk or Break-bulk Cargo (LCL)
        - Import
        - Export
      - Containerized Dangerous Cargo
        - 20 Footer Container
        - 40 Footer Container
  - **Import Processing Fee** (IPF)
  - **Customs Documentary Stamp** (CDS)
    - Formal Entry
    - Informal Entry

### Value-Added Tax (VAT)
  - Excise Tax Shipments
  - Non-Excise Tax Shipments

### Summary of Payments (SOP)
  - Covered by Letter of Credit (L/C)
  - Covered by Non-Letter of Credit
  - Covered by Informal Entry

### Container Security Fee (CSF)
  - 20 Footer Container
  - 40 Footer Container

### Pro-Rata
  - Individual Freight
  - Individual Insurance
  - Individual Dutiable Value
  - Individual Miscellaneous Expense
