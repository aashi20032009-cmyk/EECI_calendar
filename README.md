# EECI Calendar

A Flask-based web application that automatically fetches the EECI GATE coaching schedule and displays it in an interactive calendar interface.

## Features

- Automatic schedule fetching from the EECI website
- Interactive monthly calendar view
- Subject-wise schedule display
- Classroom information on click
- Timing information on click
- Responsive web interface

## Tech Stack

- Python
- Flask
- Requests
- BeautifulSoup4
- FullCalendar.js
- HTML/CSS/JavaScript

## Project Structure

```
eeci-schedule-calendar/
│
├── app.py
├── scraper.py
├── parser.py
├── events_generator.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── calendar.html
│
├── tests/
│   ├── parser_test.py
│   └── events_generator_test.py
│
└── .gitignore
```

## How It Works

1. The application fetches the latest schedule from the EECI website.
2. Schedule data is parsed into individual class dates.
3. Events are generated for each class session.
4. FullCalendar renders the events in an interactive monthly view.
5. Clicking an event displays classroom and timing details.

## Installation

Clone the repository:

```bash
git clone https://github.com/aashi20032009-cmyk/eeci-schedule-calendar.git
cd eeci-schedule-calendar
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Example Features

- View all upcoming classes in calendar format.
- Navigate between months.
- Click any class entry to view:
  - Subject
  - Classroom
  - Timing

## Future Improvements

- Event color coding by subject
- Search and filter functionality
- Weekly and daily views
- Mobile-friendly UI enhancements
- Schedule caching for faster loading
- Public deployment and custom domain

## Author

**P. Aashi Apuurvaa**

GitHub: https://github.com/aashi20032009-cmyk