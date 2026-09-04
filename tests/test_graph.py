from app.graph.attack_graph import AttackGraph
from app.models.event import SecurityEvent

from datetime import datetime


graph = AttackGraph()

event1 = SecurityEvent(
    event_id="G001",
    event_type="PORT_SCAN",
    timestamp=datetime.now(),
    source_ip="192.168.1.50",
    source_app="nmap",
    target="SSH_SERVICE",
    status="DETECTED"
)

event2 = SecurityEvent(
    event_id="G002",
    event_type="LOGIN_ATTEMPT",
    timestamp=datetime.now(),
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
    user="root"
)


graph.add_event(event1)
graph.add_event(event2)

graph.add_relationship(event1, event2, 0.97)


print("Nodes:")
print(graph.nodes)

print("\nEdges:")
print(graph.edges)