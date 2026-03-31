# Rose-Hulman Academic Calendar Converter

A Python tool that converts Rose-Hulman Institute of Technology academic calendar data into iCalendar (.ics) format for import into Google Calendar, Apple Calendar, Outlook, and other calendar applications.

## Where the Data Comes From

The calendar data is sourced from the official Rose-Hulman academic calendars published by the Office of the Registrar:

| File | Source | Description |
|------|--------|-------------|
| `2025-26_Academic_Year_Calendar.pdf` | [Rose-Hulman Registrar](https://www.rose-hulman.edu/academics/registrar/academic-calendar.html) | Official 2025-26 academic calendar PDF |
| `2026-27_Academic_Year_Calendar.pdf` | [Rose-Hulman Registrar](https://www.rose-hulman.edu/academics/registrar/academic-calendar.html) | Official 2026-27 academic calendar PDF |

The dates in the script (`rose_hulman_calendar_to_ics.py`) were manually extracted from these official PDFs and transcribed into the `CALENDAR_2025_26` and `CALENDAR_2026_27` data structures.

## Generated Calendar Files

| File | Events | Description |
|------|--------|-------------|
| `rose_hulman_2025-26.ics` | 53 | 2025-26 academic year only |
| `rose_hulman_2026-27.ics` | 56 | 2026-27 academic year only |
| `rose_hulman_2025-27.ics` | 109 | Combined 2025-27 (both years) |

## Usage

### Generate Calendars

```bash
python3 rose_hulman_calendar_to_ics.py
```

This regenerates all `.ics` files from the embedded calendar data.

### Import to Your Calendar

1. Download the desired `.ics` file
2. Import into your calendar application:
   - **Google Calendar**: Settings → Import & Export → Import
   - **Apple Calendar**: File → Import
   - **Outlook**: File → Open & Export → Import/Export

## GitHub Pages

The repository is configured with GitHub Pages (`index.html`) to provide a simple download interface for the calendar files.

## Data Coverage

Each calendar includes:

- Quarter start/end dates
- Class add/drop deadlines
- Registration periods
- Final examination dates
- Grade due dates
- Institute holidays
- Breaks (Fall, Winter, Spring, Summer)
- Special events (Homecoming, Commencement, Career Fair)
- Fee payment deadlines

## Updating for Future Years

When Rose-Hulman publishes new academic calendars:

1. Download the new PDF from the Registrar's website
2. Add it to this repository
3. Transcribe the dates into a new `CALENDAR_20XX_YY` list in `rose_hulman_calendar_to_ics.py`
4. Run the script to generate new `.ics` files
5. Update `index.html` with the new download links

## License

This project is unofficial and not affiliated with Rose-Hulman Institute of Technology. The calendar data is sourced from publicly available documents published by the university.
