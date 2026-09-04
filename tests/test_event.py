from app.models.event import SecurityEvent
from app.correlation.engine import group_by_ip
from app.ai.embeddings import get_event_embedding
from app.ai.embeddings import compare_events
from app.ai.embeddings import correlation_score


SE_1 = SecurityEvent(
    event_id="001",
    event_type="PORT_SCAN",
    timestamp="2026-08-24T10:01:00",
    source_ip="192.168.1.50",
    source_app="nmap",
    target="SSH",
    status="DETECTED"
)

SE_2 = SecurityEvent(
    event_id="002",
    event_type="LOG_IN_ATTEMPT",
    timestamp="2026-08-24T10:01:10",
    source_ip="192.168.1.50",
    source_app="ssh",
    target="SSH",
    status="FAILED",
    user="admin"
)


SE_3 = SecurityEvent(
    event_id="003",
    event_type="LOG_IN_ATTEMPT",
    timestamp="2026-08-24T10:01:50",
    source_ip="192.168.1.52",
    source_app="ssh",
    target="SSH",
    status="SUCCESS",
    user="admin"
)

# print(group_by_ip([SE_2, SE_1]))
group_by = group_by_ip([SE_2, SE_1])

# print(event_to_text(SE_3))
'''
embeddings_SE_1 = get_event_embedding(SE_1)
print(f"Embedding for SE_1: {embeddings_SE_1}")
print(f"Embedding shape for SE_1: {embeddings_SE_1.shape}")
embeddings_SE_2 = get_event_embedding(SE_2)
print(f"Embedding for SE_2: {embeddings_SE_2}")
print(f"Embedding shape for SE_2: {embeddings_SE_2.shape}")

sim = compare_events(SE_1, SE_2)
print(f"Similarity between SE_1 and SE_2: {sim}")'''

print(f"Correlation score between SE_1 and SE_2: {correlation_score(SE_1, SE_2)}")