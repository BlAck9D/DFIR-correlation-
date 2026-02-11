import os
import csv

def write_outputs(output_dir, timeline_events):
    os.makedirs(output_dir, exist_ok=True)

    # Master Timeline CSV
    with open(os.path.join(output_dir, "Master_Timeline.csv"), "w", newline='', encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Time", "Source", "Event"])

        for e in timeline_events:
            writer.writerow([
                e["time"].strftime("%Y-%m-%d %H:%M:%S"),
                e["source"],
                e["event"]
            ])

    # Incident Summary
    with open(os.path.join(output_dir, "Incident_Summary.txt"), "w", encoding="utf-8") as summary:
        summary.write("INCIDENT SUMMARY\n")
        summary.write("================\n\n")

        for e in timeline_events:
            summary.write(
                f"{e['time'].strftime('%H:%M:%S')} - {e['source']}: {e['event']}\n"
            )

    print("✅ DFIR Timeline and Incident Summary generated successfully.")
