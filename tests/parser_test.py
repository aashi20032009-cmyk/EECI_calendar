from parser import extract_dates

text = """
JUN'26:
13th, 14th
20th, 21st
26th, 27th
28th
"""

print(extract_dates(text))