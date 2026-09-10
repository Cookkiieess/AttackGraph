from datetime import datetime

from app.models.event import SecurityEvent
from app.graph.attack_graph import AttackGraph
from app.graph.chain_builder import build_attack_chain

import pickle


# Load trained model
with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)


# Create test events
event1 = SecurityEvent(
    event_id="E1",
    event_type="PORT_SCAN",
    timestamp=datetime(2026, 1, 1, 10, 0, 0),
    source_ip="192.168.1.50",
    source_app="nmap",
    target="SSH_SERVICE",
    status="DETECTED",
    user=None
)

event2 = SecurityEvent(
    event_id="E2",
    event_type="HTTP_REQUEST",
    timestamp=datetime(2026, 1, 1, 10, 0, 10),
    source_ip="192.168.1.50",
    source_app="browser",
    target="WEB_SERVER",
    status="SUCCESS",
    user="admin"
)

event3 = SecurityEvent(
    event_id="E3",
    event_type="LOGIN_ATTEMPT",
    timestamp=datetime(2026, 1, 1, 10, 0, 25),
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
    user="admin"
)

event4 = SecurityEvent(
    event_id="E4",
    event_type="FILE_ACCESS",
    timestamp=datetime(2026, 1, 1, 10, 2, 0),
    source_ip="192.168.1.50",
    source_app="explorer",
    target="FILE_SERVER",
    status="SUCCESS",
    user="admin"
)

event5 = SecurityEvent(
    event_id="E5",
    event_type="LOGIN_ATTEMPT",
    timestamp=datetime(2026, 1, 1, 10, 0, 20),
    source_ip="192.168.1.100",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
    user="admin"
)


events = [event1, event2, event3, event4, event5]


# Create graph
graph = AttackGraph()


# Build attack chain
build_attack_chain(
    events,
    model,
    graph
)


# Check that every event became a node
assert len(graph.nodes) == 5


# Display results
print("\nNodes:")
for node_id in graph.nodes:
    print(node_id)


print("\nAttack Relationships:")
for edge in graph.edges:
    print(edge)


print("\nTotal nodes:", len(graph.nodes))
print("Total attack relationships:", len(graph.edges))

print("\nTest passed!")