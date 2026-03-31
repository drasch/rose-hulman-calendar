#!/usr/bin/env python3
"""
Rose-Hulman Academic Calendar to ICS Converter

Converts Rose-Hulman Institute of Technology academic calendar data
into ICS (iCalendar) format for import into calendar applications.

Usage:
    python3 rose_hulman_calendar_to_ics.py

Output:
    - rose_hulman_2025-26.ics
    - rose_hulman_2026-27.ics
    - rose_hulman_2025-27.ics (merged)
"""

from datetime import datetime, timedelta
import uuid
from typing import List, Tuple


def generate_uid() -> str:
    """Generate a unique identifier for calendar events."""
    return str(uuid.uuid4())


def format_datetime(dt: datetime, all_day: bool = False) -> str:
    """Format datetime for ICS format."""
    if all_day:
        return dt.strftime("%Y%m%d")
    return dt.strftime("%Y%m%dT%H%M%S")


def escape_text(text: str) -> str:
    """Escape special characters in ICS text fields."""
    return text.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")


def create_ics_event(summary: str, start: datetime, end: datetime,
                     description: str = "", location: str = "", all_day: bool = False) -> str:
    """Create a single VEVENT block for ICS file."""
    uid = generate_uid()
    dtstamp = format_datetime(datetime.now())
    dtstart = format_datetime(start, all_day)
    dtend = format_datetime(end, all_day)

    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{dtstamp}",
        f"DTSTART:{dtstart}",
        f"DTEND:{dtend}",
        f"SUMMARY:{escape_text(summary)}",
    ]

    if description:
        lines.append(f"DESCRIPTION:{escape_text(description)}")
    if location:
        lines.append(f"LOCATION:{escape_text(location)}")

    lines.append("END:VEVENT")
    return "\n".join(lines)


def create_ics_header(calname: str) -> str:
    """Create ICS file header."""
    return "\n".join([
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Rose-Hulman Calendar Converter//EN",
        f"X-WR-CALNAME:{escape_text(calname)}",
        "X-WR-CALDESC:Rose-Hulman Institute of Technology Academic Calendar",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ])


def create_ics_footer() -> str:
    """Create ICS file footer."""
    return "END:VCALENDAR"


# =============================================================================
# 2025-26 Academic Year Events
# =============================================================================

CALENDAR_2025_26: List[Tuple[str, str, str, bool]] = [
    # Fall Quarter 2025
    ("New Faculty Begin", "2025-08-20", "2025-08-20", True),
    ("Opening Symposium", "2025-08-28", "2025-08-28", True),
    ("Fee Payments Due – Fall Quarter", "2025-08-29", "2025-08-29", True),
    ("New Student Orientation", "2025-08-29", "2025-09-03", True),
    ("Labor Day – Holiday", "2025-09-01", "2025-09-01", True),
    ("Classes Begin – Fall Quarter", "2025-09-04", "2025-09-04", True),
    ("Final Date to Add a Class", "2025-09-10", "2025-09-10", True),
    ("Modified Class Schedule (Convo Schedule) – Fall Career Fair", "2025-10-01", "2025-10-01", True),
    ("Homecoming", "2025-10-04", "2025-10-04", True),
    ("Fall Break – No classes", "2025-10-09", "2025-10-10", True),
    ("Midterm Progress Reports Due – Noon", "2025-10-14", "2025-10-14", True),
    ("Registration for Winter Term", "2025-10-20", "2025-10-24", True),
    ("Final Date to Drop a Course - with W grade", "2025-10-31", "2025-10-31", True),
    ("Final Examinations", "2025-11-17", "2025-11-20", True),
    ("Fee Payments Due – Winter Quarter", "2025-11-21", "2025-11-21", True),
    ("Final Grades Due & Fall Term Ends", "2025-11-24", "2025-11-24", True),

    # Winter Quarter 2025-26
    ("Classes Begin – Winter Quarter", "2025-12-01", "2025-12-01", True),
    ("Final Date to Add a Class", "2025-12-05", "2025-12-05", True),
    ("Holiday Vacation Begins", "2025-12-19", "2026-01-05", True),
    ("Martin Luther King, Jr Day – Holiday", "2026-01-19", "2026-01-19", True),
    ("Midterm Progress Reports Due – Noon", "2026-01-20", "2026-01-20", True),
    ("Registration for Spring Term", "2026-01-26", "2026-01-30", True),
    ("Final Date to Drop a Course - with W grade", "2026-02-06", "2026-02-06", True),
    ("Final Examinations", "2026-02-23", "2026-02-26", True),
    ("Fee Payments Due – Spring Quarter", "2026-02-27", "2026-02-27", True),
    ("Final Grades Due & Winter Term Ends", "2026-03-02", "2026-03-02", True),

    # Spring Quarter 2026
    ("Classes Begin – Spring Quarter", "2026-03-09", "2026-03-09", True),
    ("Final Date to Add a Class", "2026-03-13", "2026-03-13", True),
    ("Summer Registration begins", "2026-03-16", "2026-03-16", True),
    ("Spring Break", "2026-04-10", "2026-04-20", True),
    ("Midterm Progress Reports Due – Noon", "2026-04-21", "2026-04-21", True),
    ("Registration for Fall Term", "2026-05-04", "2026-05-08", True),
    ("Final Date to Drop a Course - with W grade", "2026-05-08", "2026-05-08", True),
    ("Memorial Day - Holiday", "2026-05-25", "2026-05-25", True),
    ("Final Examinations", "2026-05-26", "2026-05-29", True),
    ("Grades Due for Graduating Seniors", "2026-05-26", "2026-05-26", True),
    ("Commencement", "2026-05-30", "2026-05-30", True),
    ("Final Grades Due & Spring Term Ends", "2026-06-02", "2026-06-02", True),

    # Summer 2026
    ("Summer Session 1 Begins", "2026-06-04", "2026-06-04", True),
    ("Final Date to add Summer Session 1", "2026-06-04", "2026-06-04", True),
    ("Institute Holiday - No classes", "2026-06-19", "2026-06-19", True),
    ("Final date to drop Summer Session 1 courses", "2026-07-02", "2026-07-02", True),
    ("Institute Holiday - No classes", "2026-07-03", "2026-07-03", True),
    ("Summer Session 1 ends", "2026-07-10", "2026-07-10", True),
    ("Summer Break begins", "2026-07-13", "2026-07-13", True),
    ("Summer Session 1 final grades due by noon", "2026-07-15", "2026-07-15", True),
    ("Summer Break ends", "2026-07-17", "2026-07-17", True),
    ("Summer Session 2 begins", "2026-07-20", "2026-07-20", True),
    ("Final date to add Summer Session 2 courses", "2026-07-20", "2026-07-20", True),
    ("Final date to drop Full Summer courses", "2026-08-07", "2026-08-07", True),
    ("Final date to drop Summer Session 2 courses", "2026-08-14", "2026-08-14", True),
    ("Summer Session 2 ends", "2026-08-21", "2026-08-21", True),
    ("Summer Session 2 final grades due", "2026-08-26", "2026-08-26", True),
]

# =============================================================================
# 2026-27 Academic Year Events
# =============================================================================

CALENDAR_2026_27: List[Tuple[str, str, str, bool]] = [
    # Fall Quarter 2026
    ("New Faculty Begin", "2026-08-19", "2026-08-19", True),
    ("Opening Symposium", "2026-08-27", "2026-08-27", True),
    ("Fee Payments Due – Fall Quarter", "2026-08-28", "2026-08-28", True),
    ("New Student Orientation", "2026-08-28", "2026-09-02", True),
    ("Classes Begin – Fall Quarter", "2026-09-03", "2026-09-03", True),
    ("Labor Day - Holiday", "2026-09-07", "2026-09-07", True),
    ("Final Date to Add a Class", "2026-09-09", "2026-09-09", True),
    ("Modified Class Schedule, Career Fair", "2026-09-30", "2026-09-30", True),
    ("Homecoming", "2026-10-03", "2026-10-03", True),
    ("Fall Break – No classes", "2026-10-08", "2026-10-09", True),
    ("Midterm Progress Reports Due – Noon", "2026-10-13", "2026-10-13", True),
    ("Registration for Winter Term", "2026-10-19", "2026-10-23", True),
    ("Final Date to Drop a Course - with W grade", "2026-10-30", "2026-10-30", True),
    ("Final Examinations", "2026-11-16", "2026-11-19", True),
    ("Fee Payments Due – Winter Quarter", "2026-11-20", "2026-11-20", True),
    ("Final Grades Due & Fall Term Ends", "2026-11-23", "2026-11-23", True),

    # Winter Quarter 2026-27
    ("Classes Begin – Winter Quarter", "2026-11-30", "2026-11-30", True),
    ("Registration Deadline – 4:00 p.m.", "2026-12-02", "2026-12-02", True),
    ("Final Date to Add a Class", "2026-12-04", "2026-12-04", True),
    ("Holiday Vacation Begins", "2026-12-18", "2027-01-04", True),
    ("Martin Luther King, Jr Day - Holiday", "2027-01-18", "2027-01-18", True),
    ("Midterm Progress Reports Due – Noon", "2027-01-19", "2027-01-19", True),
    ("Registration for Spring Term", "2027-01-25", "2027-01-29", True),
    ("Final Date to Drop a Course - with W grade", "2027-02-05", "2027-02-05", True),
    ("Final Examinations", "2027-02-22", "2027-02-25", True),
    ("Fee Payments Due – Spring Quarter", "2027-02-26", "2027-02-26", True),
    ("Final Grades Due & Winter Term Ends", "2027-03-01", "2027-03-01", True),

    # Spring Quarter 2027
    ("Classes Begin – Spring Quarter", "2027-03-08", "2027-03-08", True),
    ("Registration Deadline – 4:00 p.m.", "2027-03-10", "2027-03-10", True),
    ("Final Date to Add a Class", "2027-03-12", "2027-03-12", True),
    ("Summer Registration begins", "2027-03-15", "2027-03-15", True),
    ("Spring Break", "2027-04-09", "2027-04-19", True),
    ("Midterm Progress Reports Due – Noon", "2027-04-20", "2027-04-20", True),
    ("Registration for Fall Term", "2027-05-03", "2027-05-07", True),
    ("Final Date to Drop a Course - with W grade", "2027-05-07", "2027-05-07", True),
    ("Final Examinations", "2027-05-24", "2027-05-27", True),
    ("Grades Due for Graduating Seniors", "2027-05-25", "2027-05-25", True),
    ("Fee Payments Due – Summer Sessions", "2027-05-28", "2027-05-28", True),
    ("Commencement", "2027-05-29", "2027-05-29", True),
    ("Memorial Day - Holiday", "2027-05-31", "2027-05-31", True),
    ("Final Grades Due & Spring Term Ends", "2027-06-01", "2027-06-01", True),

    # Summer 2027
    ("Summer Session 1 Begins", "2027-06-03", "2027-06-03", True),
    ("Final Date to add Summer Session 1", "2027-06-03", "2027-06-03", True),
    ("Institute Holiday - No classes", "2027-06-18", "2027-06-18", True),
    ("Final date to drop Summer Session 1 courses", "2027-07-01", "2027-07-01", True),
    ("Institute Holiday - No classes", "2027-07-02", "2027-07-02", True),
    ("Summer Session 1 ends", "2027-07-09", "2027-07-09", True),
    ("Summer Break begins", "2027-07-12", "2027-07-12", True),
    ("Summer Session 1 final grades due by noon", "2027-07-14", "2027-07-14", True),
    ("Summer Break ends", "2027-07-16", "2027-07-16", True),
    ("Summer Session 2 begins", "2027-07-19", "2027-07-19", True),
    ("Final date to add Summer Session 2 courses", "2027-07-19", "2027-07-19", True),
    ("Final date to drop Full Summer courses", "2027-08-06", "2027-08-06", True),
    ("Final date to drop Summer Session 2 courses", "2027-08-13", "2027-08-13", True),
    ("Summer Session 2 ends", "2027-08-20", "2027-08-20", True),
    ("Summer Session 2 final grades due", "2027-08-25", "2027-08-25", True),
]


def generate_ics_file(events: List[Tuple[str, str, str, bool]],
                      calname: str, output_path: str) -> None:
    """Generate an ICS file from a list of events."""
    lines = [create_ics_header(calname)]

    for summary, start_str, end_str, all_day in events:
        start = datetime.strptime(start_str, "%Y-%m-%d")
        # For end date, add one day if it's an all-day event to make it inclusive
        end = datetime.strptime(end_str, "%Y-%m-%d")
        if all_day:
            end = end + timedelta(days=1)

        event = create_ics_event(summary, start, end, all_day=all_day)
        lines.append(event)

    lines.append(create_ics_footer())

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Generated: {output_path} ({len(events)} events)")


def main():
    """Main entry point."""
    print("Rose-Hulman Academic Calendar to ICS Converter")
    print("=" * 50)

    # Generate 2025-26 calendar
    generate_ics_file(
        CALENDAR_2025_26,
        "Rose-Hulman 2025-26",
        "rose_hulman_2025-26.ics"
    )

    # Generate 2026-27 calendar
    generate_ics_file(
        CALENDAR_2026_27,
        "Rose-Hulman 2026-27",
        "rose_hulman_2026-27.ics"
    )

    # Generate merged calendar (2025-27)
    merged_events = CALENDAR_2025_26 + CALENDAR_2026_27
    generate_ics_file(
        merged_events,
        "Rose-Hulman 2025-27",
        "rose_hulman_2025-27.ics"
    )

    print("=" * 50)
    print("Done! Import the .ics files into your calendar application.")


if __name__ == "__main__":
    main()
