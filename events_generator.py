from parser import extract_dates

def build_events(date_text,
                 subject,
                 classroom,
                 timing):

    events = []

    dates = extract_dates(date_text)

    for date in dates:

        events.append({
            "title": subject,
            "start": date,
            "extendedProps": {
        "room": classroom,
        "timing": timing
    }
        })

    return events