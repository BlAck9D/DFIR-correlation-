from datetime import datetime

def parse_time(raw_time):
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H-%M-%S",
        "%d-%m-%Y %H:%M:%S",
        "%d-%m-%Y %H:%M",
        "%d-%m-%Y %H-%M-%S",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(raw_time.strip(), fmt)
        except ValueError:
            continue
    return None
