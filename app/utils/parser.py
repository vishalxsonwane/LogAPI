from dateutil import parser as date_parser

def parse_log_line(line: str):
    """
    Parses log line: Timestamp\tLevel\tComponent\tMessage
    """
    parts = line.strip().split("\t", 3)

    if len(parts) != 4:
        return None

    timestamp = date_parser.parse(parts[0])
    level = parts[1]
    component = parts[2]
    message = parts[3]

    return timestamp, level, component, message
