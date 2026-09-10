from datetime import datetime, timedelta

from app.models.event import SecurityEvent
from app.graph.candidates import find_candidates


base_time = datetime(2026, 9, 7, 10, 0, 0)

event1 = SecurityEvent(
    event_id="E1",
    event_type="PORT_SCAN",
    timestamp=base_time,
    source_ip="192.168.1.50",
    source_app="nmap",
    target="SSH_SERVICE",
    status="DETECTED",
)

event2 = SecurityEvent(
    event_id="E2",
    event_type="HTTP_REQUEST",
    timestamp=base_time + timedelta(seconds=10),
    source_ip="192.168.1.50",
    source_app="browser",
    target="WEB_SERVER",
    status="SUCCESS",
)

event3 = SecurityEvent(
    event_id="E3",
    event_type="LOGIN_ATTEMPT",
    timestamp=base_time + timedelta(seconds=25),
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
)

event4 = SecurityEvent(
    event_id="E4",
    event_type="FILE_ACCESS",
    timestamp=base_time + timedelta(seconds=120),
    source_ip="192.168.1.50",
    source_app="explorer",
    target="FILE_SERVER",
    status="SUCCESS",
)

event5 = SecurityEvent(
    event_id="E5",
    event_type="LOGIN_ATTEMPT",
    timestamp=base_time + timedelta(seconds=20),
    source_ip="192.168.1.100",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
)


events = [event1, event2, event3, event4, event5]

candidates = find_candidates(events, event1)

print("Candidates:")
for candidate in candidates:
    print(candidate.event_id)

assert candidates == [event2, event3]

print("Test passed!")