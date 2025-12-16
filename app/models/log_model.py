from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    id: str
    timestamp: datetime
    level: str
    component: str
    message: str
