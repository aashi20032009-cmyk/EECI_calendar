from flask import Flask, render_template

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from events_generator import build_events

app = Flask(__name__)


def get_schedule_events():

    driver = webdriver.Chrome()

    driver.get("https://www.eecigate.in/schedule/")

    time.sleep(2)

    table = driver.find_element(By.ID, "tablepress-19")

    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    events = []

    for row in rows:

        cols = row.find_elements(By.TAG_NAME, "td")

        if len(cols) != 4:
            continue

        date_text = cols[0].text

        subject = " ".join(cols[1].text.split())

        classroom = cols[2].text

        timing = " ".join(cols[3].text.split())

        events.extend(
            build_events(
                date_text,
                subject,
                classroom,
                timing
            )
        )

    driver.quit()

    return events


@app.route("/")
def home():

    events = get_schedule_events()

    return render_template(
        "calendar.html",
        events=events
    )


if __name__ == "__main__":
    app.run(debug=True)