'''
    format:
    <CAMPUS(2)>.<SCHOOL(2)>.<PROGRAMME(1)><DURATION(1)><BRANCH(3)><START_YEAR(2)><ROLL_NO(3)>
'''

import re

SCHOOL_NAMES = {
    "EN": "Engineering",
    "SC": "Computing",
    "AI": "Artificial Intelligence",
}

PROGRAMME_TYPES = {
    "U": "Undergraduate",
    "P": "Postgraduate",
    "D": "Doctorate",
    "R": "Research",
}


def parse_roll_number(roll_number: str) -> dict:
    default_result = {
        "campus": "Unknown",
        "school": "Unknown",
        "programmeType": "Unknown",
        "duration": 0,
        "branch": "Unknown",
        "startYear": 0,
        "graduationYear": 0,
        "rollCall": "",
        "isValid": False,
    }

    if not roll_number:
        return default_result

    clean_roll = roll_number.replace(".", "").upper()

    pattern = r"^([A-Z]{2})([A-Z]{2})([UPDR])([\d*])([A-Z]{3})(\d{2})(\d{3})$"
    match = re.match(pattern, clean_roll)

    if not match:
        return default_result

    campus, school, programme, duration, branch, year_digits, roll_call = match.groups()

    programme_type = PROGRAMME_TYPES.get(programme, "Unknown")
    is_indefinite = duration == "*"
    duration_int = None if is_indefinite else int(duration)
    start_year = 2000 + int(year_digits)
    graduation_year = start_year + duration_int if duration_int else None

    return {
        "campus": campus,
        "school": SCHOOL_NAMES.get(school, school),
        "programmeType": programme_type,
        "duration": duration_int,
        "branch": branch,
        "startYear": start_year,
        "graduationYear": graduation_year,
        "rollCall": roll_call,
        "isValid": True,
    }


def get_graduation_year(roll_number: str) -> int | None:
    info = parse_roll_number(roll_number)
    return info["graduationYear"] if info["isValid"] else None


def get_batch_display(roll_number: str) -> str:
    year = get_graduation_year(roll_number)
    return f"Class of {year}" if year else "N/A"


def get_programme_display(roll_number: str) -> str:
    info = parse_roll_number(roll_number)
    if not info["isValid"] or info["programmeType"] == "Unknown":
        return "N/A"
    duration = (
        f"{info['duration']}-Year" if info["duration"] else "Indefinite Duration"
    )
    return f"{duration} {info['programmeType']}"
