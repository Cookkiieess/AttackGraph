from pydantic import BaseModel
from datetime import datetime

class SecurityEvent(BaseModel):
    event_id: str
    event_type: str
    timestamp: datetime
    source_ip: str
    source_app: str
    target: str
    status: str
    user: str | None = None  # Optional field for user information
    external_ip: str | None = None  # Optional field for external IP address
    direction: str | None = None  # Optional field for direction of the event (incoming/outgoing)
    data: dict | None = None  # Optional field for additional event data