import re

date_text = """
JUN'26:
13th, 14th
20th, 21st
26th, 27th
28th
"""

lines = [line.strip() for line in date_text.splitlines() if line.strip()]

month = "06"
year = "2026"

dates = []

for line in lines[1:]:

    nums = re.findall(r"\d+", line)

    for n in nums:
        dates.append(f"{year}-{month}-{int(n):02d}")

print(dates)