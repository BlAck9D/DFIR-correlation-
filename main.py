from dfir_core.reader import read_csv
from dfir_core.timeline import build_timeline
from dfir_core.writer import write_outputs

INPUT_DIR = "input_data"
OUTPUT_DIR = "output"

all_events = []

# Email
all_events += read_csv(
    INPUT_DIR,
    "email.csv",
    "Email",
    lambda r: r.get("event", "Email event")
)

# MFT
all_events += read_csv(
    INPUT_DIR,
    "mft.csv",
    "FileSystem",
    lambda r: f"{r.get('action','Action')} file {r.get('filepath','Unknown')}"
)

# Logs
all_events += read_csv(
    INPUT_DIR,
    "logs.csv",
    "WindowsLog",
    lambda r: r.get("description", "Log event")
)

# Memory
all_events += read_csv(
    INPUT_DIR,
    "memory.csv",
    "Memory",
    lambda r: f"{r.get('process','Process')} - {r.get('detail','Detail')}"
)

# Network
all_events += read_csv(
    INPUT_DIR,
    "network.csv",
    "Network",
    lambda r: f"Connection to {r.get('destination','Unknown')} with {r.get('bytesout','0')} bytes sent"
)

timeline = build_timeline(all_events)
write_outputs(OUTPUT_DIR, timeline)
