dates = [
    '2026-06-13',
    '2026-06-14',
    '2026-06-20',
    '2026-06-21',
    '2026-06-26',
    '2026-06-27',
    '2026-06-28'
]

events = []

for date in dates:

    events.append({
        "title": "Electro Magnetics",
        "start": date,
        "room": "Class 1",
        "timing": "9.15 am to 6.30 pm"
    })

for event in events:
    print(event)