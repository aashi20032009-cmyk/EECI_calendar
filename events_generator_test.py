from events_generator import build_events

events = build_events(
    """
    JUN'26:
    13th, 14th
    20th, 21st
    """,
    "Electro Magnetics",
    "Class 1",
    "9.15 am to 6.30 pm"
)

for e in events:
    print(e)