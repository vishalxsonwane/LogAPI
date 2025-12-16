import os
import uuid
from app.config import LOG_DIR
from app.utils.parser import parse_log_line

def read_all_logs():
    logs = []
    log_id_counter = 1

    for file in os.listdir(LOG_DIR):
        file_path = os.path.join(LOG_DIR, file)

        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r") as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    timestamp, level, component, message = parsed
                    logs.append({
                        "id": str(log_id_counter),
                        "timestamp": timestamp,
                        "level": level,
                        "component": component,
                        "message": message
                    })
                    log_id_counter += 1

    return logs
