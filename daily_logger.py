
import datetime

def log_entry(entry):
    with open("activity_summary.txt", "a") as log:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        log.write(f"[{time}] {entry}\n")
