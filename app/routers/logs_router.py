from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from app.services.log_service import filter_logs, get_stats, get_log_by_id
from app.models.log_model import LogEntry

router = APIRouter(prefix="/logs")


@router.get("/", response_model=list[LogEntry])
def get_logs(
    level: Optional[str] = None,
    component: Optional[str] = None,
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None)
):
    try:
        logs = filter_logs(level, component, start_time, end_time)
        return logs
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid query parameters")


@router.get("/stats")
def get_logs_stats():
    return get_stats()


@router.get("/{log_id}", response_model=LogEntry)
def get_log(log_id: str):
    log = get_log_by_id(log_id)
    if log:
        return log
    raise HTTPException(status_code=404, detail="Log entry not found")
