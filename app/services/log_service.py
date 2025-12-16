from typing import Optional
from datetime import datetime
from app.utils.file_reader import read_all_logs

def filter_logs(
    level: Optional[str],
    component: Optional[str],
    start_time: Optional[datetime],
    end_time: Optional[datetime]
):
    logs = read_all_logs()

    result = logs

    if level:
        result = [log for log in result if log["level"].upper() == level.upper()]
    
    if component:
        result = [log for log in result if log["component"].lower() == component.lower()]

    if start_time:
        result = [log for log in result if log["timestamp"] >= start_time]

    if end_time:
        result = [log for log in result if log["timestamp"] <= end_time]

    return result


def get_stats():
    logs = read_all_logs()

    total = len(logs)

    count_by_level = {}
    count_by_component = {}

    for log in logs:
        level = log["level"]
        component = log["component"]

        count_by_level[level] = count_by_level.get(level, 0) + 1
        count_by_component[component] = count_by_component.get(component, 0) + 1

    return {
        "total_entries": total,
        "by_level": count_by_level,
        "by_component": count_by_component,
    }


def get_log_by_id(log_id: str):
    logs = read_all_logs()
    for log in logs:
        if log["id"] == log_id:
            return log
    return None
