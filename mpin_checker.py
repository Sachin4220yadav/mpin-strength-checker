# mpin_checker.py

# List of frequently used and easily guessable MPINs
COMMON_PIN_LIST = [
    "0000", "1111", "1234", "1212", "7777", "1004", "2000",
    "4444", "2222", "6969", "9999", "3333", "5555", "6666", "1122"
]

def is_common_pin(pin):
    return pin in COMMON_PIN_LIST

def generate_date_patterns(date):
    day = date[:2]
    month = date[2:4]
    year = date[4:]
    year_short = year[-2:]

    # Create common combinations used by users
    patterns = [
        day + month,
        month + day,
        year_short + month,
        month + year_short,
        day + month + year_short,
        year,
        day + month + year  # For 6-digit PINs
    ]
    return patterns

def find_demographic_matches(pin, self_dob, spouse_dob, anniversary):
    issues = []

    if pin in generate_date_patterns(self_dob):
        issues.append("DEMOGRAPHIC_DOB_SELF")
    if pin in generate_date_patterns(spouse_dob):
        issues.append("DEMOGRAPHIC_DOB_SPOUSE")
    if pin in generate_date_patterns(anniversary):
        issues.append("DEMOGRAPHIC_ANNIVERSARY")

    return issues

def check_pin_strength(pin, self_dob, spouse_dob, anniversary):
    reasons = []

    if is_common_pin(pin):
        reasons.append("COMMONLY_USED")

    reasons += find_demographic_matches(pin, self_dob, spouse_dob, anniversary)

    status = "WEAK" if reasons else "STRONG"
    return status, reasons

