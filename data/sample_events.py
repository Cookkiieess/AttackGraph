from app.models.event import SecurityEvent


SE_1 = SecurityEvent(
    event_id="101",
    event_type="PORT_SCAN",
    timestamp="2026-08-25T10:01:00",
    source_ip="192.168.1.50",
    source_app="nmap",
    target="SSH",
    status="DETECTED"
)

SE_2 = SecurityEvent(
    event_id="102",
    event_type="LOGIN_ATTEMPT",
    timestamp="2026-08-25T10:01:10",
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH",
    status="FAILED",
    user="admin"
)

SE_3 = SecurityEvent(
    event_id="103",
    event_type="LOGIN_ATTEMPT",
    timestamp="2026-08-25T10:01:20",
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH",
    status="SUCCESS",
    user="admin"
)

SE_4 = SecurityEvent(
    event_id="104",
    event_type="FILE_ACCESS",
    timestamp="2026-08-25T18:30:00",
    source_ip="192.168.1.80",
    source_app="powershell",
    target="C:\\Users\\Public\\report.pdf",
    status="SUCCESS",
    user="john"
)