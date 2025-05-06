fdata = [
    {
        "request_type": "Adjustment",
        "definition": "Adjustments are changes made to financial records or allocations due to errors, reassignments, or contractual updates. These do not involve actual cash flow but update ledger balances.",
        "sub_types": [
            {
                "name": "Reallocation Fees",
                "definition": "Movement of previously booked fees (e.g., agency, arrangement) from one facility or borrower to another.",
            },
            {
                "name": "Amendment Fees",
                "definition": "Adjusting fees imposed due to loan contract changes (e.g., margin or tenor changes).",
            },
            {
                "name": "Accounting Correction",
                "definition": "Rectification of misbooked entries such as wrong amounts, dates, or entities.",
            },
        ],
        "attributes": ["Amount", "From Account", "To Account", "Transaction Date", "Reference"],
        "examples": [
            {
                "sub_type": "Accounting Correction",
                "email": "Please correct the amount on transaction #12345 from $1,000 to $1,100.",
                "justification": "The email explicitly mentions correcting an amount, which falls under accounting correction.",
            },
            {
                "sub_type": "Reallocation Fees",
                "email": "Move the arrangement fee from borrower A to borrower B.",
                "justification": "The email requests movement of a fee from one borrower to another"
            }
        ],
    },
    {
        "request_type": "Money Movement Outbound",
        "definition": "Outbound movements involve the transfer of funds from the borrower or facility to external parties (e.g., lenders, agents, service providers) for loan servicing.",
        "sub_types": [
            {
                "name": "Principal",
                "definition": "Scheduled or early repayment of the original borrowed amount.",
            },
            {
                "name": "Interest",
                "definition": "Periodic payment based on the outstanding principal and applicable rate.",
            },
            {
                "name": "Fees",
                "definition": "Payments for ancillary services like commitment, arrangement, or legal fees.",
            },
        ],
        "attributes": ["Amount", "From Account", "To Account", "Payment Date"],
        "examples": [
            {
                "sub_type": "Principal",
                "email": "Please pay $10,000 towards the principal of loan #67890.",
                "justification": "The email specifies a payment towards the principal amount of a loan.",
            },
            {
                "sub_type": "Interest",
                "email": "Send the interest payment of $500 for loan #67890.",
                "justification": "The email requests sending an interest payment."
            }
        ],
    },
    {
        "request_type": "Money Movement Inbound",
        "definition": "Inbound money movements refer to funds credited to the borrower's loan account or facility for repayment, prepayment, or deposits.",
        "sub_types": [
            {
                "name": "Prepayment",
                "definition": "Voluntary early repayment, often reducing future interest.",
            },
            {
                "name": "Cash Contribution",
                "definition": "Deposits made to cover upcoming obligations (e.g., interest or fees).",
            },
            {
                "name": "Reimbursement",
                "definition": "Repayment from third parties or affiliates for previously settled amounts.",
            },
        ],
        "attributes": ["Amount", "Account Number", "Transaction Date"],
        "examples": [
            {
                "sub_type": "Prepayment",
                "email": "I'd like to prepay $2,000 on my loan.",
                "justification": "The email indicates an early payment on a loan.",
            },
            {
                "sub_type": "Cash Contribution",
                "email": "Deposit of $1000 to cover upcoming fees",
                "justification": "The email mentions a deposit to cover fees."
            }
        ],
    },
    {
        "request_type": "Fee Payment",
        "definition": "Refers to the settlement of various fees associated with managing, arranging, or servicing a facility.",
        "sub_types": [
            {
                "name": "Arrangement Fee",
                "definition": "One-time fee paid for structuring and arranging the loan.",
            },
            {
                "name": "Agency Fee",
                "definition": "Compensation to the agent bank responsible for administrative roles in syndicated loans.",
            },
            {
                "name": "Commitment Fee",
                "definition": "Fee charged on the unused portion of a committed line of credit.",
            },
        ],
        "attributes": ["Payee Name", "Account Number", "Amount", "Payment Date"],
        "examples": [
            {
                "sub_type": "Arrangement Fee",
                "email": "Please process the $25,000 arrangement fee.",
                "justification": "The email requests processing of an arrangement fee.",
            },
            {
                "sub_type": "Agency Fee",
                "email": "Pay the agency fee of $10,000 to ABC Bank.",
                "justification": "The email requests payment of an agency fee"
            }
        ],
    },
    {
        "request_type": "Closing Notice",
        "definition": "Notification regarding the closure of a loan or credit facility, which may be due to repayment, expiration, or early termination.",
        "sub_types": [
            {
                "name": "Timebound",
                "definition": "Closure effective on a specific date, often planned in advance.",
            },
            {
                "name": "Facility Full Repayment",
                "definition": "Final closure triggered by the borrower having repaid all obligations.",
            },
            {
                "name": "Mutual Agreement",
                "definition": "Closure due to negotiated terms between borrower and lender.",
            },
        ],
        "attributes": ["Loan Number", "Closure Date"],
        "examples": [
            {
                "sub_type": "Timebound",
                "email": "Please be advised that loan #12345 will close on 2024-12-31.",
                "justification": "The email provides a specific date for loan closure.",
            },
            {
                "sub_type": "Facility Full Repayment",
                "email": "Loan #12345 is closed as the borrower has repaid all obligations.",
                "justification": "The email states the loan is closed due to full repayment."
            }
        ],
    },
    {
        "request_type": "Cashless Roll",
        "definition": "The continuation of a loan through extension or renewal, without actual cash movement — typically used for short-term or revolving credit.",
        "sub_types": [
            {
                "name": "Interest Rollover",
                "definition": "Accrued interest is rolled into the new period rather than paid.",
            },
            {
                "name": "Principal Rollover",
                "definition": "Outstanding principal remains without a new disbursement.",
            },
            {
                "name": "Same-Day Rollover",
                "definition": "Maturity and new drawdown happen on the same day.",
            },
        ],
        "attributes": ["Loan Number", "Rollover Date"],
        "examples": [
            {
                "sub_type": "Interest Rollover",
                "email": "Roll the accrued interest on loan #23456 into the new period.",
                "justification": "The email requests that accrued interest is rolled over.",
            },
            {
                "sub_type": "Principal Rollover",
                "email": "Roll the principal amount of loan #23456.",
                "justification": "The email requests that the principal amount is rolled over"
            }
        ],
    },
    {
        "request_type": "Loan Drawdown",
        "definition": "A request by a borrower to withdraw funds under an approved facility.",
        "sub_types": [
            {
                "name": "Term Loan",
                "definition": "A draw from a facility with fixed repayment terms and schedule.",
            },
            {
                "name": "Revolving Credit Facility (RCF)",
                "definition": "Withdrawal under a facility with flexible usage and repayment.",
            },
            {
                "name": "Delayed Draw Facility",
                "definition": "Pre-approved loan amount drawn at a later date, usually under specified conditions.",
            },
        ],
        "attributes": ["Loan Number", "Amount", "Drawdown Date"],
        "examples": [
            {
                "sub_type": "Term Loan",
                "email": "Draw down $50,000 from term loan #34567.",
                "justification": "The email requests a drawdown from a term loan.",
            },
            {
                "sub_type": "Revolving Credit Facility (RCF)",
                "email": "Requesting a $20,000 drawdown from the RCF.",
                "justification": "The email requests a drawdown from a revolving credit facility"
            }
        ],
    },
    {
        "request_type": "Repayment Instruction",
        "definition": "Directives from the borrower to repay loan obligations — either regularly scheduled or discretionary.",
        "sub_types": [
            {
                "name": "Scheduled Repayment",
                "definition": "As defined in the amortization schedule.",
            },
            {
                "name": "Voluntary Prepayment",
                "definition": "Borrower opts to repay earlier than required, potentially avoiding interest.",
            },
            {
                "name": "Mandatory Prepayment",
                "definition": "Triggered by covenant breaches or events like asset sales.",
            },
        ],
        "attributes": ["Loan Number", "Amount", "Payment Date"],
        "examples": [
            {
                "sub_type": "Voluntary Prepayment",
                "email": "I want to prepay $10,000 on loan #45678.",
                "justification": "The email expresses a desire to prepay a loan.",
            },
            {
                "sub_type": "Scheduled Repayment",
                "email": "Make the scheduled repayment of $5000 for loan #45678",
                "justification": "The email requests a scheduled repayment"
            }
        ],
    },
    {
        "request_type": "Interest Accrual",
        "definition": "Accumulation of interest over a specific time period, often used for accounting, reporting, and planning.",
        "sub_types": [
            {
                "name": "Month-End Accrual",
                "definition": "Calculated for closing books at the end of a reporting period.",
            },
            {
                "name": "Mid-Period Estimate",
                "definition": "Estimated accruals for forecasting purposes.",
            },
            {
                "name": "Accrued but Unpaid",
                "definition": "Interest recorded but not yet settled in cash.",
            },
        ],
        "attributes": ["Loan Number", "Accrual Period"],
        "examples": [
            {
                "sub_type": "Month-End Accrual",
                "email": "Calculate the month-end interest accrual for loan #56789.",
                "justification": "The email requests month-end interest accrual calculation.",
            },
            {
                "sub_type": "Mid-Period Estimate",
                "email": "Provide a mid-period estimate of interest accrual.",
                "justification": "The email requests an estimate of interest accrual"
            }
        ],
    },
    {
        "request_type": "Facility Amendment",
        "definition": "Legal and operational updates to the loan agreement, often requiring lender consent.",
        "sub_types": [
            {
                "name": "Interest Margin Change",
                "definition": "Revising the spread applied over the benchmark rate.",
            },
            {
                "name": "Tenor Extension",
                "definition": "Changing the maturity or duration of the loan.",
            },
            {
                "name": "Collateral Update",
                "definition": "Revising or substituting the pledged asset(s).",
            },
        ],
        "attributes": ["Loan Number", "Amendment Details"],
        "examples": [
            {
                "sub_type": "Interest Margin Change",
                "email": "Requesting a change in the interest margin for loan #67890.",
                "justification": "The email requests a change to the interest margin.",
            },
            {
                "sub_type": "Tenor Extension",
                "email": "Extend the tenor of loan #67890 by 6 months.",
                "justification": "The email requests an extension to the loan tenor."
            }
        ],
    },
    {
        "request_type": "Commitment Charge",
        "definition": "Fee charged to borrowers for the lender's commitment to provide funds, even if unused.",
        "sub_types": [
            {
                "name": "Undrawn Facility",
                "definition": "Fee charged on the portion of the facility not drawn.",
            },
            {
                "name": "Utilization Fee",
                "definition": "Tiered fee based on the percentage of the facility drawn.",
            },
            {
                "name": "Step-Up Fee",
                "definition": "Increasing fee as the facility usage crosses predefined thresholds.",
            },
        ],
        "attributes": ["Loan Number", "Fee Amount", "Fee Period"],
        "examples": [
            {
                "sub_type": "Undrawn Facility",
                "email": "Calculate the commitment charge on the undrawn portion of loan #78901.",
                "justification": "The email asks for calculation of a fee on the undrawn portion.",
            },
            {
                "sub_type": "Utilization Fee",
                "email": "Charge the utilization fee for loan #78901.",
                "justification": "The email requests a utilization fee to be charged."
            }
        ],
    },
    {
        "request_type": "Reconciliation",
        "definition": "Process of matching and verifying transaction records between internal systems and external counterparts (e.g., custodians, banks).",
        "sub_types": [
            {
                "name": "Ledger Mismatch",
                "definition": "Errors or inconsistencies in financial records.",
            },
            {
                "name": "Bank Statement Reconciliation",
                "definition": "Comparison of ledger entries against actual cash movement.",
            },
            {
                "name": "Break Resolution",
                "definition": "Investigation and resolution of discrepancies.",
            },
        ],
        "attributes": ["Account Number", "Discrepancy Details"],
        "examples": [
            {
                "sub_type": "Ledger Mismatch",
                "email": "There is a mismatch in the ledger for account #89012.",
                "justification": "The email reports a mismatch in the ledger.",
            },
            {
                "sub_type": "Bank Statement Reconciliation",
                "email": "Reconcile the bank statement for account #89012.",
                "justification": "The email requests reconciliation of a bank statement."
            }
        ],
    },
    {
        "request_type": "Document Request",
        "definition": "Request to provide or retrieve official documentation associated with financial transactions or compliance.",
        "sub_types": [
            {
                "name": "Facility Agreement",
                "definition": "Core legal document outlining terms of the facility.",
            },
            {
                "name": "Payment Confirmation",
                "definition": "Proof that a payment has been made or received.",
            },
            {
                "name": "Audit Trail",
                "definition": "Historical logs for internal or regulatory audits.",
            },
        ],
        "attributes": ["Loan Number", "Document Type"],
        "examples": [
            {
                "sub_type": "Facility Agreement",
                "email": "Please provide the facility agreement for loan #90123.",
                "justification": "The email requests a facility agreement document.",
            },
            {
                "sub_type": "Payment Confirmation",
                "email": "Requesting payment confirmation for transfer #12345",
                "justification": "The email requests a payment confirmation"
            }
        ],
    },
    {
        "request_type": "Rate Fixing",
        "definition": "Setting the applicable interest rate (e.g., SOFR, EURIBOR) for a specific loan period.",
        "sub_types": [
            {
                "name": "LIBOR/SOFR Fixing",
                "definition": "Determining the daily or periodic benchmark rate.",
            },
            {
                "name": "Day Count Convention",
                "definition": "Adjusting the accrual calculation method (e.g., ACT/360).",
            },
            {
                "name": "Fixing Confirmation",
                "definition": "Formal notification of the fixed rate for a term.",
            },
        ],
        "attributes": ["Loan Number", "Rate Type", "Fixing Date"],
        "examples": [
            {
                "sub_type": "LIBOR/SOFR Fixing",
                "email": "Fix the SOFR rate for loan #01234.",
                "justification": "The email requests fixing of the SOFR rate.",
            },
            {
                "sub_type": "Fixing Confirmation",
                "email": "Please confirm the fixed rate for loan #01234",
                "justification": "The email requests confirmation of a fixed rate"
            }
        ],
    },
    {
        "request_type": "KYC/Compliance Update",
        "definition": "Ensuring that borrower and facility-level records meet ongoing regulatory standards.",
        "sub_types": [
            {
                "name": "Sanctions Screening",
                "definition": "Checking against OFAC, UN, EU, and other watchlists.",
            },
            {
                "name": "Document Expiry",
                "definition": "Alert and renewal of expiring ID, licenses, or documentation.",
            },
            {
                "name": "Ownership Structure Update",
                "definition": "Reflecting changes in beneficial ownership or shareholding.",
            },
        ],
        "attributes": ["Borrower Name", "Update Details"],
        "examples": [
            {
                "sub_type": "Sanctions Screening",
                "email": "Perform sanctions screening for borrower 'XYZ Corp'.",
                "justification": "The email requests sanctions screening.",
            },
            {
                "sub_type": "Document Expiry",
                "email": "Update expiring documents for borrower 'XYZ Corp'",
                "justification": "The email requests an update for expiring documents"
            }
        ],
    },
    {
        "request_type": "Covenant Monitoring",
        "definition": "Ongoing assessment of the borrower's compliance with loan covenants.",
        "sub_types": [
            {
                "name": "DSCR Reporting",
                "definition": "Monitoring Debt Service Coverage Ratio to ensure financial health.",
            },
            {
                "name": "Leverage Ratio Compliance",
                "definition": "Ensuring the borrower's debt-to-equity or debt-to-EBITDA stays within limits.",
            },
            {
                "name": "Quarterly Certification",
                "definition": "Regular compliance confirmation by the borrower.",
            },
        ],
        "attributes": ["Loan Number", "Reporting Period"],
        "examples": [
            {
                "sub_type": "DSCR Reporting",
                "email": "Provide DSCR reporting for loan #11223 for Q1 2024.",
                "justification": "The email requests DSCR reporting.",
            },
            {
                "sub_type": "Leverage Ratio Compliance",
                "email": "Check the leverage ratio compliance for loan #11223",
                "justification": "The email requests a check on leverage ratio"
            }
        ],
    },
    {
        "request_type": "Collateral Movement",
        "definition": "Administrative handling of assets pledged against the facility.",
        "sub_types": [
            {
                "name": "Margin Call",
                "definition": "Request for additional collateral when value drops below threshold.",
            },
            {
                "name": "Collateral Release",
                "definition": "Removal of lien on asset after repayment.",
            },
            {
                "name": "Collateral Substitution",
                "definition": "Swap of pledged asset with another of similar value.",
            },
        ],
        "attributes": ["Loan Number", "Collateral Details"],
        "examples": [
            {
                "sub_type": "Margin Call",
                "email": "Issue a margin call for loan #12345.",
                "justification": "The email requests a margin call.",
            },
            {
                "sub_type": "Collateral Release",
                "email": "Release the collateral for loan #12345",
                "justification": "The email requests collateral release"
            }
        ],
    },
    {
        "request_type": "Holiday Notification",
        "definition": "Adjustment or communication related to non-working days that impact financial operations.",
        "sub_types": [
            {
                "name": "Payment Rescheduling",
                "definition": "Moving payment due dates that fall on holidays.",
            },
            {
                "name": "Business Day Adjustment",
                "definition": "Shifting operational activities.",
            },
            {
                "name": "Rate Fix Delay",
                "definition": "Postponement of benchmark fixing.",
            },
        ],
        "attributes": ["Holiday Name", "Impacted Activity"],
        "examples": [
            {
                "sub_type": "Payment Rescheduling",
                "email": "Reschedule payments due to the upcoming holiday.",
                "justification": "The email requests rescheduling of payments.",
            },
            {
                "sub_type": "Rate Fix Delay",
                "email": "Delay the rate fixing due to the holiday.",
                "justification": "The email requests a delay in rate fixing"
            }
        ],
    },
    {
        "request_type": "Break Cost Calculation",
        "definition": "Calculation of financial penalties or charges due to early termination of loan agreements or associated derivatives.",
        "sub_types": [
            {
                "name": "Early Repayment Penalty",
                "definition": "Fee for repaying a loan before maturity.",
            },
            {
                "name": "Hedge Break Fee",
                "definition": "Cost for terminating an interest rate swap or hedge prematurely.",
            },
            {
                "name": "Unwind Cost",
                "definition": "Total cost incurred when ending the financial agreement before its term.",
            },
        ],
        "attributes": ["Loan Number", "Calculation Type"],
        "examples": [
            {
                "sub_type": "Early Repayment Penalty",
                "email": "Calculate the early repayment penalty for loan #13456.",
                "justification": "The email requests calculation of an early repayment penalty.",
            },
            {
                "sub_type": "Hedge Break Fee",
                "email": "Calculate the hedge break fee.",
                "justification": "The email requests calculation of a hedge break fee."
            }
        ],
    },
    {
        "request_type": "System Booking",
        "definition": "Recording of financial transactions or changes in the system of record (loan management, treasury, etc.).",
        "sub_types": [
            {
                "name": "New Facility Setup",
                "definition": "Initial booking of a loan or facility with full terms and conditions.",
            },
            {
                "name": "Rate Update",
                "definition": "Adjusting the system with current interest rate data.",
            },
            {
                "name": "Booking Correction",
                "definition": "Fixing errors in previously recorded transactions.",
            },
        ],
        "attributes": ["Loan Number", "Booking Details"],
        "examples": [
            {
                "sub_type": "New Facility Setup",
                "email": "Book the new facility with the following terms...",
                "justification": "The email requests booking a new facility.",
            },
            {
                "sub_type": "Rate Update",
                "email": "Update the rate for loan #14567 in the system.",
                "justification": "The email requests an update of the interest rate."
            }
        ],
    },
]
