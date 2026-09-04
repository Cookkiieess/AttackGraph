import pickle
from datetime import datetime, timedelta

from app.graph.attack_graph import AttackGraph
from app.graph.builder import build_relationship
from app.models.event import SecurityEvent


# Load trained model
with open("data/model.pkl", "rb") as f:
    model = pickle.load(f)


# Create two related security events
event1 = SecurityEvent(
    event_id="B001",
    event_type="PORT_SCAN",
    timestamp=datetime.now(),
    source_ip="192.168.1.50",
    source_app="nmap",
    target="SSH_SERVICE",
    status="DETECTED",
    user=None,
)


event2 = SecurityEvent(
    event_id="B002",
    event_type="LOGIN_ATTEMPT",
    timestamp=datetime.now() + timedelta(seconds=20),
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH_SERVICE",
    status="FAILED",
    user="admin",
)


# Create graph
graph = AttackGraph()


# Build relationship between the events
build_relationship(
    graph,
    model,
    event1,
    event2
)


# Inspect graph
print("Nodes:")
print(graph.nodes)

print("\nEdges:")
print(graph.edges)