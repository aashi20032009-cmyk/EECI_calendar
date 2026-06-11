import re

MONTHS = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12"
}


def extract_dates(date_text):

    lines = [
        line.strip()
        for line in date_text.splitlines()
        if line.strip()
    ]

    month_line = lines[0]

    match = re.search(r"([A-Z]{3})'(\d{2})", month_line)

    month = MONTHS[match.group(1)]
    year = "20" + match.group(2)

    dates = []

    for line in lines[1:]:

        nums = re.findall(r"\d+", line)

        for n in nums:

            dates.append(
                f"{year}-{month}-{int(n):02d}"
            )

    return dates