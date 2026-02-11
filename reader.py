import os
import csv
from .parser import parse_time

def read_csv(input_dir, file_name, source_name, message_builder):
    events = []
    file_path = os.path.join(input_dir, file_name)

    if not os.path.exists(file_path):
        print(f"⚠️ Skipping {file_name} (not found)")
        return events

    with open(file_path, newline='', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        reader.fieldnames = [fn.strip().lower() for fn in reader.fieldnames]

        for row in reader:
            row = {k.strip().lower(): v.strip() for k, v in row.items()}

            if "timestamp" not in row:
                continue

            event_time = parse_time(row["timestamp"])
            if not event_time:
                continue

            event_message = message_builder(row)

            events.append({
                "time": event_time,
                "source": source_name,
                "event": event_message
            })

    return events
